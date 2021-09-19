from os.path import isfile
from os.path import join

from flask import *

from content import load_content

if not isfile('.env'):
    raise Exception(
        'Missing .env file, please add a .env file in your root directory.')

content = load_content("content.yml")

# firebase imports (should be done after dotenv validation)
from firebase import user
from firebase import tools as fbtools

app = Flask(__name__, template_folder='src')
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


def start():
    user.login("allah@gmail.comuwu", "uwu123")
    app.run(debug=True, threaded=True)


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
        return fbtools.isauthorized(level, uid)

    def c_user():
        try:
            return fbtools.get_doc(u'users', user.current_uid())
        except Exception:
            return None

    return dict(is_signed_in=is_signed_in,
                current_pfp=current_pfp,
                user_elevations=user_elevations,
                authorized=authorized,
                c_user=c_user)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('./screens/index.html',
                           subpage=request.args.get('goto'))


@app.route('/profile/me', methods=['GET', 'POST'])
def profile_me():
    # TODO: Check if user signed in, redirect to /register
    return redirect(f'/profile/{user.current_uid()}')


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


@app.route('/profile/<uid>')
def user_profile(uid):
    # try fetching data from the uid using fbtools and redirect to / if Exception
    try:
        user_data = fbtools.get_doc(u'users', uid)
        if user_data["elevation"] != [] and user_data["ban"] is False:
            # user is elevated, return profile page
            return render_template('./screens/profile.html',
                                   user_data=user_data)
        else:
            raise Exception("Unelevated user profile")
    except Exception:
        # render a profile doesn't exists or is deleted message if user_data=None
        return render_template('./screens/profile.html', user_data=None)


def md_html(md_str):
    return markdown(md_str)


@app.route('/article/<uid>')
def article(uid):
    # try fetching data from the uid using fbtools and redirect to / if Exception
    try:
        article = fbtools.get_doc(u'articles', uid)
        if article["is_approved"] is True:
            # Article approved and published, return the content
            return render_template('./screens/article.html',
                                   article=article,
                                   article_body=md_html(article["body"]))
        else:
            raise Exception("Non-approved article")
    except Exception:
        # Render an article not found message
        return render_template('./screens/article.html', article=None)


if __name__ == '__main__':
    start()
