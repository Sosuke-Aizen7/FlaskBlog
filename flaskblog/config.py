import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # postgresql://blog_hd8c_user:luXxHSLXW7KbUgYg3lT0UTRf6dRcHaQi@dpg-csjgf2u8ii6s73d3r9lg-a.oregon-postgres.render.com/blog_hd8c
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = 'jbid fweh fsok gxeo'