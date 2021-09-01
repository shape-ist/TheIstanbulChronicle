from os.path import isfile
from os.path import join

from flask import *
from flask_easymde import EasyMDE
from flaskext.markdown import Markdown

from content import load_content

if not isfile('.env'):
    raise Exception(
        'Missing .env file, please add a .env file in your root directory.')

content = load_content("content.yml")

# firebase imports (should be done after dotenv validation)
from firebase import user

app = Flask(__name__, template_folder='src')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FLASK_ENV'] = 'development'
Markdown(app)
mde = EasyMDE(app)

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
        return redirect(url, code=code)
"""


@app.context_processor
def utility_processor():
    def get_display_name(amount, currency=u'$'):
        return u'{1}{0:.2f}'.format(amount, currency)

    def allah(a):
        return a

    def is_signed_in():
        return user.is_signed_in()

    return dict(get_display_name=get_display_name,
                allah=allah,
                is_signed_in=is_signed_in)


@app.route('/', methods=['GET', 'POST'])
def home():
    # TODO: get multiple POST methods for login and register here
    """
    if request.method == "POST" and param="login": ???
        login_email = request.form.get("name-login-email")
        login_password = request.form.get("name-login-password")
        user.login(login_email, login_password)
    if request.method == 'POST' and param="register": ???
        register_email = request.form.get("name-register-email")
        register_password = request.form.get("name-register-password")
        register_displayname = request.form.get("name-register-displayname")
        user.register(register_email, register_password, register_displayname)
    """

    return render_template('./index.html', subpage=request.args.get('goto'))


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    from firebase.pfp import update_pfp, get_default
    """ 
    if request.method == "POST":
        imagefile = request.files.get('pfpinput', '')
    update_pfp('QuVb0qlU6GfW9CYW9iuIXGRVlhp2') """

    # pfp = '' results in default pfp, enter a valid url for a custom pfp.
    return render_template(
        './screens/profile.html',
        pfp='',
        displayname='Barış İnandıoğlu',
        elevations=['S'],
        location='Istanbul',
        phone='543 863 6598',
        email='baris@gmail.com',
        bio=
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    )


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
    # TODO: check access of user before returning template of elevated html pages.
    # TODO: ERROR 403-like page IF ACCESS DENIED
    # TODO: add different favicon on elevated pages. (see elevated directory)
    return render_template('./screens/elevated/write.html')


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


if __name__ == '__main__':
    print("app started")
    app.run(debug=True, threaded=True)