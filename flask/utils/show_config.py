# to run from webapp
import os
import sys
path_to_webapp = os.path.join(os.path.dirname(os.getcwd()), 'webapp')
sys.path.insert(0,path_to_webapp)
from flask_blog import create_app
app = create_app()
for c in app.config:
    print(c,"                         ",app.config[c])