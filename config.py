import os
from mail_config import default_user, default_pw
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'app.db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 10
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1 
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or default_user
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or default_pw
    ADMINS = ['maschaefer713@gmail.com']

## setup for gmail
# set MAIL_SERVER=smtp.googlemail.com
# set MAIL_PORT=587
# set MAIL_USE_TLS=1
# set MAIL_USERNAME=<your-gmail-username>
# set MAIL_PASSWORD=<your-gmail-password>