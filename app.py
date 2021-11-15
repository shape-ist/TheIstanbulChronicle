# test

from datetime import datetime
from os.path import isfile
from os.path import join
from markdown import markdown

from flask import *
from flask_caching import Cache
from flask_socketio import SocketIO, send
from authlib.integrations.flask_client import OAuth
import json

from content import load_content
import g_auth

if not isfile('.env'):
    print(
        'WARN: Missing .env file, please add a .env file in your root directory.'
    )

content = load_content("content.yml")
earlyaccess = False

# firebase imports (should be done after dotenv validation)
from firebase import user as fbuser
from firebase import tools as fbtools
from firebase import paginate
from firebase import search as fbsearch

app = Flask(__name__, template_folder='src')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FLASK_ENV'] = 'development'
app.config['DEBUG'] = True
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 1800
app.secret_key = g_auth.secret_key

sio = SocketIO(app, debug=True, threaded=True)
oauth = OAuth(app)

google = oauth.register(**g_auth.config)

CATS = {}

with open('cats.json') as f:
    CATS = json.load(f)


def md_html(md_str):
    return markdown(md_str)


@app.context_processor
def utility_processor():
    def is_signed_in():
        return fbuser.is_signed_in()

    def current_pfp():
        try:
            return fbtools.get_doc(u'users', fbuser.current_uid())['pfp']
        except Exception:
            return ''

    def user_elevations():
        try:
            return fbtools.get_doc(u'users', fbuser.current_uid())['elevation']
        except Exception:
            return []

    def authorized(level, uid=fbuser.current_uid()):
        try:
            return fbtools.isauthorized(level, uid)
        except Exception:
            return False

    def c_user():
        try:
            return fbtools.get_doc(u'users', fbuser.current_uid())
        except Exception:
            return None

    def unix_time(time):
        return datetime.fromtimestamp(time).strftime('%d/%m/%Y')

    def cats():
        return CATS

    return dict(is_signed_in=is_signed_in,
                current_pfp=current_pfp,
                user_elevations=user_elevations,
                authorized=authorized,
                c_user=c_user,
                unix_time=unix_time,
                cats=cats)


@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        subpage = request.args.get('goto') if earlyaccess is not True else None
        init_pagi = paginate.paginate('articles', 'timestamp', l=5, o='DESC')
        for i in init_pagi['data'][1:]:
            i['body'] = i['body'].strip().replace("\n",
                                                  "")[:150].rsplit(' ', 1)[0]
        return render_template('./screens/index.html',
                               subpage=subpage,
                               h=init_pagi)
    except Exception as e:
        return f"Something went wrong: {e}"


@app.route('/greet')
def greet():
    return dict(session)['profile']


@app.route('/login/google')
def google_auth():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    user = oauth.google.userinfo()
    session['profile'] = user_info
    session.permanent = True
    fbuser.google_user_doc(user_info)
    return redirect('/')


@app.route('/profile/my/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')


@app.route('/profile/my/delete')
def delete_user():
    try:
        fbuser.delete_user()
        return redirect('/profile/my/logout')
    except Exception:
        return "Couldn't delete your account"


@app.route('/profile/me', methods=['GET', 'POST'])
def current_user_profile_redir():
    try:
        cuid = fbuser.current_uid()
        if cuid != None:
            return redirect(f'/profile/{cuid}')
        return redirect('/login')
    except Exception:
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
    if fbuser.user_exists(uid):
        return render_template('./screens/verify.html',
                               verification_text=content["verification_text"])
    return redirect("/")


@app.route('/favicon.png')
def favicon():
    return send_from_directory(join(app.root_path, 'static'),
                               'favicon.png',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/write')
def write():
    # TODO: add different favicon on elevated pages. (see elevated directory)

    if fbtools.isauthorized('W', fbuser.current_uid()):
        return render_template('./screens/elevated/write.html')
    return forbidden(Exception("User not authorized"))


@app.route('/legal/terms-and-conditions')
def terms():
    with open('terms.md', 'r') as f:
        tac = md_html(f.read())
    return render_template('./screens/legal/terms-and-conditions.html',
                           updated="2021-09-06",
                           tac=tac)


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
    return redirect(
        "/?goto=register") if earlyaccess is not True else redirect('/')


@app.route('/login')
def login():
    return redirect("/?goto=login") if earlyaccess is not True else redirect(
        '/')


@app.route('/profile/my/edit', methods=['GET', 'POST'])
def profile_edit():
    if earlyaccess is True: return redirect('/')
    try:
        if (fbuser.current_uid() is None or fbtools.get_doc(
                u'users', fbuser.current_uid())['elevation'] == []):
            return redirect('/login')
        if request.method == "POST":
            fbtools.update_fields(
                'users',
                fbuser.current_uid(),
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
    except Exception:
        return redirect('/login')


@app.route('/profile/<uid>')
def user_profile(uid):
    try:
        user_data = fbtools.get_doc(u'users', uid)
        if user_data['elevation'] == []:
            raise Exception()
        return render_template('./screens/profile.html', user_data=user_data)
    except Exception:
        return render_template('./screens/profile_not_found.html')


@app.route('/article/<auid>')
def article_page(auid):
    # try fetching data from the uid using fbtools and redirect to / if Exception
    """ try:
        article = fbtools.get_doc(u'articles', uid)
        if article["is_approved"] is True:
            # Article approved and published, return the content
            return render_template('./screens/article.html', article=article)
        else:
            raise Exception("Non-approved article")
    except Exception:
        # Render an article not found message
        return render_template('./screens/article.html', article=None) """
    try:
        article = fbtools.get_doc(u'articles', auid)
        article['writer'] = article['writer'].get().to_dict()
        return render_template('./screens/article.html', article=article)
    except Exception:
        return render_template('./screens/article_not_found.html')


@app.route('/profile/my/rmpfp')
def rmpfp():
    try:
        fbtools.update_fields(u'users', fbuser.current_uid(), {u'pfp': ''})
    except Exception:
        pass
    return ("current user pfp reset")


@app.route('/profile/my/delete-acc')
def rmacc():
    # TODO: #52 this should open up a verification page. using the button, get a post method and when method='post', call remove account function.
    return ("alla")


@app.route('/api/pagi/<coll>/<sort>/q')
def api_pagi(coll, sort):
    return paginate.paginate(coll, sort, **dict(request.args))


@app.route('/search/<kw>')
def search(kw):
    return fbsearch.search_article(kw)


@sio.on('pagiRequest')
def pagi_request(data):
    send(paginate.paginate('articles', 'timestamp', l=10, o='desc', i=data))


def start():
    # fbuser.register("dmeoeom@gdgd.com", "passssword", "name")
    # fbuser.login("dmeoeom@gdgd.com", "passssword")
    # app.run(debug=True, threaded=True)
    sio.run(app)


def uuid():
    from firebase.setup import auth
    try:
        return auth.current_user['localId']
    except Exception:
        return None


if __name__ == '__main__':
    start()
