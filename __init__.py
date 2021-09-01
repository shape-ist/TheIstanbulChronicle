from os.path import isfile
from os.path import join

from flask import *
from flask_easymde import EasyMDE
from flaskext.markdown import Markdown

from content import load_content

app = Flask(__name__, template_folder='src')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FLASK_ENV'] = 'development'
Markdown(app)
mde = EasyMDE(app)


@app.context_processor
def utility_processor():
    def format_price(amount, currency=u'€'):
        return u'{0:.2f}{1}'.format(amount, currency)

    return dict(format_price=format_price)