import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwtsecretkey')
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=int(os.environ.get('JWT_REFRESH_TOKEN_EXPIRES', 24)))
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 24)))

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://root:Arun%40123@localhost/edu')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    # Flask Admin Panel Settings (Optional)
    FLASK_ADMIN_SWATCH = 'cerulean'
