from flask import *
from os.path import join
from os.path import isfile
from flask_easymde import EasyMDE
from flaskext.markdown import Markdown
from content import load_content

if not isfile('.env'):
    raise Exception(
        'Missing .env file, please add a .env file in your root directory.')

content = load_content("content.yml")

from firebase import setup
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


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        login_email = request.form.get("name-login-email")
        login_password = request.form.get("name-login-password")
        user.login(login_email, login_password)

    return render_template('./index.html')


@app.route('/profile')
def profile():
    return render_template('./screens/profile.html')


@app.route('/about')
def about():
    return render_template('./screens/about.html',
                           about_text=content["about_text"])


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        register_email = request.form.get("name-register-email")
        register_password = request.form.get("name-register-password")
        register_displayname = request.form.get("name-register-displayname")
        user.register(register_email, register_password, register_displayname)
    return render_template('./screens/register.html')


@app.route('/contribute')
def contribute():
    return render_template('./screens/contr.html')


@app.route('/verify')
def verify():
    return render_template('./screens/verify.html',
                           verification_text=content["verification_text"])


@app.route('/favicon.png')
def favicon():
    return send_from_directory(join(app.root_path, 'static'),
                               'favicon.png',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/write')
def write():
    # TODO: check access of user before returning template of elevated html pages.
    # ERROR 403 IF ACCESS DENIED
    # TODO: add different favicon on elevated pages.
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


if __name__ == '__main__':
    print("app started")
    app.run(debug=True)
