from os import getenv
from dotenv import load_dotenv

config = {
    "name": 'google',
    "client_id": getenv('googleClientId'),
    "client_secret": getenv('googleClientSecret'),
    "access_token_url": 'https://accounts.google.com/o/oauth2/token',
    "access_token_params": None,
    "authorize_url": 'https://accounts.google.com/o/oauth2/auth',
    "authorize_params": None,
    "api_base_url": 'https://www.googleapis.com/oauth2/v1/',
    "userinfo_endpoint": 'https://openidconnect.googleapis.com/v1/userinfo',
    "client_kwargs": {
        'scope': 'openid email profile'
    },
}

secret_key = getenv('googleSecretAppKey')