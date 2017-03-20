import os
basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = basedir + '/app/static/uploads/'
SECRET_KEY = 'many random bytes'
MONGODB_DB = 'worddb'
