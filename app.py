from flask import *
from os.path import join
from flaskext.markdown import Markdown
from firebase import setup
from firebase import user

app = Flask(__name__, template_folder='src')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FLASK_ENV'] = 'development'
Markdown(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        login_email: str = request.form.get("name-login-email")
        login_password: str = request.form.get("name-login-password")
        user.login(login_email, login_password)

    return render_template('./index.html')


@app.route('/profile')
def profile():
    return render_template('./screens/profile.html')


@app.route('/about')
def about():
    return render_template('./screens/about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        register_email: str = request.form.get("name-register-email")
        register_password: str = request.form.get("name-register-password")
        register_displayname: str = request.form.get(
            "name-register-displayname")
        user.register(register_email, register_password, register_displayname)
    return render_template('./screens/register.html')


@app.route('/contribute')
def contribute():
    return render_template('./screens/contr.html')


@app.route('/favicon.png')
def favicon():
    return send_from_directory(join(app.root_path, 'static'),
                               'favicon.png',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/legal/license')
def license():
    return render_template('./legal/LICENSE.html')


@app.route('/legal/terms-and-conditions')
def terms():
    return render_template('./legal/terms-and-conditions.html',
                           updated="2021-09-06")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('./err/404.html'), 404


if __name__ == '__main__':
    print("app started")
    app.run(debug=True)
