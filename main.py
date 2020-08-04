from flask import Flask
from flask import render_template, request, redirect, url_for, flash, jsonify

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
from datetime import date
import os
import datetime
import sqlite3

DATABASE = 'C:/Users/johnk/Documents/GitHub/hello-world/Database/nutrition.db'

todaysdate = date.today()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/johnk/Documents/GitHub/hello-world/Database/nutrition.db'
# app.config['UPLOAD_FOLDER'] = legalAidUploadFolder
db = SQLAlchemy(app)

engine = create_engine('sqlite:///C:/Users/johnk/Documents/GitHub/hello-world/Database/nutrition.db')
db.Model.metadata.reflect(db.engine)
metadata = MetaData(bind=engine)

@app.route('/')
def hello_world():
    documents = engine.execute('select * from documents')

    return render_template('nutrition.html', documents = documents)

@app.route('/caleb')
def caleb():
    return render_template('caleb.html')

@app.route('/createdocument')
def createdocument():
    documentNumber = engine.execute("select MAX(documentId) from documents")
    row = documentNumber.fetchone()
    maxRow = row[0] + 1
    engine.execute('insert into documents (documentId) values(?)', maxRow)
    documents = engine.execute('select * from documents')
    #return render_template('caleb.html')

    return redirect(url_for('caleb'))


if __name__ == '__main__':
    app.run(debug=True)


