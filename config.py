import os
from datetime import timedelta
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-12345'

    # determine database URI, prefer env var (Render/Heroku/Neon)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    if not SQLALCHEMY_DATABASE_URI:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'jobscout.db')

    # SQLAlchemy requires postgresql:// scheme rather than postgres://
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://', 1)

    # ensure SSL mode for Neon if not already present
    if 'postgres' in SQLALCHEMY_DATABASE_URI and 'sslmode' not in SQLALCHEMY_DATABASE_URI:
        separator = '&' if '?' in SQLALCHEMY_DATABASE_URI else '?'
        SQLALCHEMY_DATABASE_URI = f"{SQLALCHEMY_DATABASE_URI}{separator}sslmode=require"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session & Persistence Settings
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_PERMANENT = True

    UPLOAD_FOLDER = os.path.join(basedir, 'backend', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
    GOOGLE_CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"

    THEME_COLORS = {
        'jacarta': '#3A345B',
        'pearly_purple': '#BA71A2',
        'queen_pink': '#F3C8DD'
    }