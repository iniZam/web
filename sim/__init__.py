import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login  import LoginManager


UPLOAD_FOLDER = 'sim/pdf'
ALLOWED_EXTENSIONS = ['pdf']

app = Flask('__name__', template_folder='sim/templates', static_folder="sim/static")
app.config['SECRET_KEY']="anjay"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sim_pengaduan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)


from sim.admin.routes import radmin
app.register_blueprint(radmin)