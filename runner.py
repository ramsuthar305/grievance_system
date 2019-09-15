from eve import Eve
from flask import render_template,request,redirect,url_for, session, escape
from eve.auth import BasicAuth
from eve.methods.get import get_internal
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from werkzeug import secure_filename
from bson import regex
from random import randint
import json,pathlib,hashlib
import requests,random,datetime,os
import re
import smtplib
import math
import smtplib
from werkzeug import secure_filename

port = 5000
host = '0.0.0.0'

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return username == 'root' and password == '22oct1997'

app = Eve(__name__, auth=MyBasicAuth)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = '5234124584324'

headers = {'Authorization': 'Basic cm9vdDoyMm9jdDE5OTc=', 'Content-Type':'application/json'}

app.config['MONGO_HOST'] = '165.22.100.196'
app.config['MONGO_PORT'] = '27017'
app.config['MONGO_DBNAME'] = 'nibodh'
app.config['MONGO_USERNAME'] = 'root'
app.config['MONGO_PASSWORD'] = '22oct1997'


UPLOAD_FOLDER = "./static/uploads/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload')
def upload():
    return render_template('add.html')
@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        print('\n\n\n\nbruuuhh in \n\n\n\n')
        f = request.files['file']
        print('saved$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4')
        f.save(secure_filename(f.filename))
        return f.filename

@app.route('/records')
def records():
    return render_template('tables.html')

@app.route("/smd")
def index():
    laude="kunj"
    return render_template('edit.html',laude = laude)


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
