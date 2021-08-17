from flask import *
from os.path import join
from firebase import *
from flaskext.markdown import Markdown

app = Flask(__name__, template_folder='src')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FLASK_ENV'] = 'development'
Markdown(app)

db = firebase_init()


@app.route('/')
def home():
    return render_template('./screens/index.html')


@app.route('/profile')
def profile():
    print(db.collection(u'users').document(auth.current_user['localId']))
    # if request.method == "POST":
    return render_template('./screens/profile.html')


@app.route('/about')
def about():
    return render_template('./screens/about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email: str = request.form.get("email_field")
        password: str = request.form.get("password_field")
        display_name: str = request.form.get("displayName")
        print(email, password, display_name)

        Register(email, password, display_name)

    return render_template('./screens/register.html')


@app.route('/contribute')
def contribute():
    return render_template('./screens/contr.html')


@app.route('/favicon.png')
def favicon():
    return send_from_directory(join(app.root_path, 'static'), 'favicon.png', mimetype='image/vnd.microsoft.icon')


@app.route('/legal/license')
def license():
    return render_template('./legal/LICENSE.html')


@app.route('/legal/terms-and-conditions')
def terms():
    return render_template('./legal/terms-and-conditions.html', updated="2021-09-06")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('./err/404.html'), 404


if __name__ == '__main__':
    print("app started")
    app.run(debug=True)
