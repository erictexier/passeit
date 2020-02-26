import os
import json

CONF_FILE = "/etc/config_flask.json"

if os.path.exists(CONF_FILE):
    with open(CONF_FILE, "r") as config_file:
        data = json.load(config_file)
else:
    data = {
        "file" : "",
        "SECRET_KEY" : "db1f5dd00c812fd540d72835d77743a2",
        "SQLALCHEMY_DATABASE_URI" : "sqlite:///site.db",
        "EMAIL_USER" : "erictexier@gmail.com",
        "EMAIL_PASS" : "toto1234",
        "EMAIL_SERVER" : "smtp.gmail.com",
        "EMAIL_USE_SSL" : True,
        "EMAIL_PORT" : 587,
        "POSTGRES_USER" : "devopsuser",
        "POSTGRES_PW" : "devops",
        "POSTGRES_URL" : "localhost",
        "POSTGRES_DB" : "flaskprofiledb",
        "POSTGRES_PORT" : 5432
        }

class Config(object):
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    SECRET_KEY = data.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = data.get("SQLALCHEMY_DATABASE_URI")
    MAIL_USERNAME = data.get("EMAIL_USER","no_user")
    MAIL_PASSWORD = data.get("EMAIL_PASS","no_pass")
    MAIL_SERVER = data.get('EMAIL_SERVER')
    MAIL_USE_TLS = data.get('EMAIL_USE_SSL')
    MAIL_PORT = data.get('EMAIL_PORT')
    if data.get("file") == CONF_FILE:
        # setting for remote
        SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{url}:{pt}/{db}'.format(
                                user = data.get("POSTGRES_USER", "devopsuser"),
                                pw = data.get("POSTGRES_PW", "devops"),
                                url = data.get("POSTGRES_URL", "localhost"),
                                pt = data.get("POSTGRES_PORT", 5432),
                                db = data.get("POSTGRES_DB", "flaskprofiledb"))