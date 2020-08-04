from flask import Flask
from flask import render_template, request, redirect, url_for, flash, jsonify

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table



from datetime import date
import os


import datetime


#import flask_sqlalchemy
#import SQLalchemy



from flask import g

DATABASE = 'C:/Users/chris/Documents/GitHub/spa/Flask/Database/thelaw.db'
todaysdate = date.today()


import sqlite3
legalAidUploadFolder = 'C:/Users/chris/Documents/GitHub/spa/Flask/static/docs/legalAid/'
casesrootfolder = 'C:\\Users\\chris\\Documents\\GitHub\\spa\\Flask\\static\\docs\\'
ALLOWED_EXTENSIONS  = {'.pdf'}
DATABASE = 'C:/Users/Chris/PycharmProjects/jobcosting/nutrition.db'

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Chris/PycharmProjects/jobcosting/nutrition.db'
# app.config['UPLOAD_FOLDER'] = legalAidUploadFolder
db = SQLAlchemy(app)


engine = create_engine('sqlite:///C:/Users/Chris/PycharmProjects/jobcosting/nutrition.db')
db.Model.metadata.reflect(db.engine)
metadata = MetaData(bind=engine)

@app.route('/')
def hello_world():
    documents = engine.execute('select * from documents')

    return render_template('nutrition.html', documents = documents)


