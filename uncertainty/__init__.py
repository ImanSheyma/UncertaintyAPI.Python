from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/uncertainty'
db = SQLAlchemy(app)

from uncertainty import indexes
from uncertainty import routes