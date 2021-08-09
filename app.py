from flask import *
from os import path

app = Flask(__name__,
            template_folder='src')

@app.route('/')
def home():
    return render_template('./screens/index.html')

@app.route('/about')
def about():
    return render_template('./screens/about.html')

@app.route('/favicon.png')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
    'favicon.png',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)