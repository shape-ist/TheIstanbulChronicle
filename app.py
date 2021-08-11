from flask import *
from os import path

app = Flask(__name__, template_folder='src')


@app.route('/')
def home():
    return render_template('./screens/index.html')


@app.route('/about')
def about():
    return render_template('./screens/about.html')


@app.route('/register')
def register():
    return render_template('./screens/register.html')


@app.route('/contribute')
def contribute():
    return render_template('./screens/contr.html')


@app.route('/favicon.png')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'favicon.png',
                               mimetype='image/vnd.microsoft.icon')


# not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('./err/404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)