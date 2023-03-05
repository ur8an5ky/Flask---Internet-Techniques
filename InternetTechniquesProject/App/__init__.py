from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://u0urbanski:0urbanski@localhost/u0urbanski' # 'postgresql://username:password@server/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '082493b92811db16ce037695'
db = SQLAlchemy(app)
login_manager = LoginManager(app)


from App import routes