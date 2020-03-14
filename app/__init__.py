from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = './app/static/photos'
#location where profile pictures are stored 
app = Flask(__name__)
app.config.from_object(__name__)#allow to configura gobla variables  such as uploads_folder
app.config['SECRET_KEY'] = 'Sup3r$3cretke#@#^26l#)('
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URL')
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dev:@Links1010@localhost/project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
db = SQLAlchemy(app)
from app import views