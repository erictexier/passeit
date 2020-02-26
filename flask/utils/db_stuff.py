# to be run from the flask app interatively the first time 
from flask_blog import create_app, db
app = create_app()
app.app_context().push()
db.create_all()