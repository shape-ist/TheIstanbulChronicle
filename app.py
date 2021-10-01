from os.path import isfile
from os.path import join
from datetime import datetime

from flask import *
from flask_socketio import SocketIO, emit

from content import load_content

if not isfile('.env'):
    raise Exception(
        'Missing .env file, please add a .env file in your root directory.')

content = load_content("content.yml")

# firebase imports (should be done after dotenv validation)
from firebase import user
from firebase import tools as fbtools
from firebase import paginate

app = Flask(__name__, template_folder='src')
sio = SocketIO(app, debug=True, threaded=True)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FLASK_ENV'] = 'development'

# TODO: might be useful in the future
# use to pass article content to article page as a kwarg though article id?
# https://root/a=article_id
# login_arg = request.args.get('login')
"""
TODO: !!!important!!!
UNCOMMENT THIS ON PRODUCTION FOR SECURE SSL CONNECTIONS

@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code = code)
"""


@app.context_processor
def utility_processor():
    def is_signed_in():
        return user.is_signed_in()

    def current_pfp():
        try:
            return fbtools.get_doc(u'users', user.current_uid())['pfp']
        except Exception:
            return ''

    def user_elevations():
        try:
            return fbtools.get_doc(u'users', user.current_uid())['elevation']
        except Exception:
            return []

    def authorized(level, uid=user.current_uid()):
        try:
            return fbtools.isauthorized(level, uid)
        except:
            return False

    def c_user():
        try:
            return fbtools.get_doc(u'users', uuid())
        except Exception:
            return 'cu'

    def unix_time(time):
        return datetime.fromtimestamp(time).strftime('%d/%m/%Y')

    return dict(is_signed_in=is_signed_in,
                current_pfp=current_pfp,
                user_elevations=user_elevations,
                authorized=authorized,
                c_user=c_user,
                unix_time=unix_time)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        for _ in range(1000):
            print(request.form)
        if request.form['job'] == 'login':
            print("login sex")
        elif request.form['job'] == 'register':
            print("register sex")
        else:
            raise Exception('Authentication Failed')
    init_pagi = paginate.paginate('articles', 'timestamp', l=5, o='DESC')
    return render_template('./screens/index.html',
                           subpage=request.args.get('goto'),
                           h=init_pagi['data'])
    # TODO: #59 implement a something went wrong page here. Since the api can return an error, we should be able to catch it.


@app.route('/profile/me', methods=['GET', 'POST'])
def current_user_profile_redir():
    try:
        cuid = user.current_uid()
        if cuid != None: return redirect(f'/profile/{cuid}')
        else: return redirect('/login')
    except:
        return redirect('/login')


@app.route('/profile')
def profile_redir():
    return redirect("/profile/me")


@app.route('/user')
def user_redir():
    return redirect("/profile/me")


@app.route('/account')
def account_redir():
    return redirect("/profile/me")


@app.route('/me')
def me_redir():
    return redirect("/profile/me")


@app.route('/profile/my')
def profile_my():
    return redirect("/profile/me")


@app.route('/my')
def my_redir():
    return redirect("/profile/me")


@app.route('/about')
def about():
    return render_template('./screens/about.html',
                           about_text=content["about_text"])


@app.route('/contribute')
def contribute():
    return render_template('./screens/contr.html')


@app.route('/verify')
# return redirect if uid param is not istype(int)
def verify():
    uid = request.args.get('uid')
    if user.user_exists(uid):
        return render_template('./screens/verify.html',
                               verification_text=content["verification_text"])
    else:
        return redirect("/")


@app.route('/favicon.png')
def favicon():
    return send_from_directory(join(app.root_path, 'static'),
                               'favicon.png',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/write')
def write():
    # TODO: add different favicon on elevated pages. (see elevated directory)

    if fbtools.isauthorized('W', user.current_uid()):
        return render_template('./screens/elevated/write.html')
    else:
        return forbidden(Exception("User not authorized"))


@app.route('/legal/license')
def license():
    return render_template('./screens/legal/LICENSE.html')


@app.route('/legal/terms-and-conditions')
def terms():
    return render_template('./screens/legal/terms-and-conditions.html',
                           updated="2021-09-06")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('./err/404.html',
                           message=content["404_message"]), 404


@app.errorhandler(403)
def forbidden(e):
    return render_template('./err/403.html',
                           message=content["403_message"]), 403


@app.route('/register')
def register():
    return redirect("/?goto=register")


@app.route('/login')
def login():
    return redirect("/?goto=login")


@app.route('/profile/my/edit', methods=['GET', 'POST'])
def profile_edit():
    try:
        if (user.current_uid() is None or fbtools.get_doc(
                u'users', user.current_uid())['elevation'] == []):
            return redirect('/login')
        if request.method == "POST":
            fbtools.update_fields(
                'users',
                user.current_uid(),
                {
                    # TODO: #51 add pfp post method here too
                    u'email_public':
                    request.form.get("profile-edit-email-public") == 'on',
                    u'bio':
                    request.form.get("profile-edit-bio").strip(),
                    u'phone':
                    request.form.get("profile-edit-phone").strip(),
                    u'location':
                    request.form.get("profile-edit-location").strip(),
                    u'name':
                    request.form.get("profile-edit-name").strip(),
                },
            )
        return render_template('./screens/profile_edit.html')
    except:
        return redirect('/login')


@app.route('/profile/<uid>')
def user_profile(uid):

    try:
        user_data = fbtools.get_doc(u'users', uid)
        if user_data['elevation'] == []:
            raise Exception()
        else:
            return render_template('./screens/profile.html',
                                   user_data=user_data)
    except:
        return render_template('./screens/profile_not_found.html')


def md_html(md_str):
    return markdown(md_str)


@app.route('/article/<uid>')
def article_page(uid):
    # try fetching data from the uid using fbtools and redirect to / if Exception
    try:
        article = fbtools.get_doc(u'articles', uid)
        if article["is_approved"] is True:
            # Article approved and published, return the content
            return render_template('./screens/article.html', article=article)
        else:
            raise Exception("Non-approved article")
    except Exception:
        # Render an article not found message
        return render_template('./screens/article.html', article=None)


@app.route('/profile/my/rmpfp')
def rmpfp():
    try:
        fbtools.update_fields(u'users', user.current_uid(), {u'pfp': ''})
    except:
        pass
    return ("current user pfp reset")


@app.route('/profile/my/delete-acc')
def rmacc():
    # TODO: #52 this should open up a verification page. using the button, get a post method and when method='post', call remove account function.
    return ("alla")


@app.route('/api/pagi/<coll>/<sort>/q')
def api_pagi(coll, sort):
    return paginate.paginate(coll, sort, **dict(request.args))


@sio.on('pushPagi')
def push_pagi():
    emit('i emmitted this neg', ('foo', 'bar', json), namespace='/uwu')


@sio.on('pagiRequest')
def pagi_request(data):
    print('received message: ' + str(data))
    push_pagi()


def start():
    # user.register("dmeoeom@gdgd.com", "passssword", "name")
    user.login("dmeoeom@gdgd.com", "passssword")
    # app.run(debug=True, threaded=True)
    sio.run(app)


def uuid():
    from firebase.setup import auth
    try:
        return auth.current_user['localId']
    except:
        return None


if __name__ == '__main__':
    start()