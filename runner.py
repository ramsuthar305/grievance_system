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
import requests,random,os
from datetime import datetime
import re
import smtplib
import math
import smtplib
from werkzeug import secure_filename
import matplotlib.pyplot as plt
import reverse_geocoder as rg


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


def reverseGeocode(coordinates):
    ret=''
    result = rg.search(coordinates)
    print('\n'*20+'result:',result[0])
    for i in range(len(result)):
        ret+=result[i]['name']
        ret+=', '+result[i]['admin1']
        ret+=', '+result[i]['admin2']
        ret+=', '+result[i]['cc']
    return ret

@app.route('/upload')
def upload():
    return render_template('add.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        db = app.data.driver.db.client['nibodh']
        print('\n\n\n\nbruuuhh in \n\n\n\n')
        f = request.files['file']
        gid=request.form['gid']
        print('\n\n\n\n\ngid:',gid)
        user=request.form['user']
        print('\n\n\n\n\nuser:',user)
        type=request.form['type']
        print('\n\n\n\n\ntype:',type)
        print('saved$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4')
        f.save(os.path.join( app.config['UPLOAD_FOLDER'], secure_filename(f.filename) ))
        db.grievance.insert_one({"image_link":f.filename,
        "grievance_id":gid,
        "user_id":user,
        "grievance_type":type,
        "area":"wahi",
        "latitude":"null",
        "longitude":"null",
        "assigned_authority":"null",
        "assigned_date":str(datetime.now()),
        "status":"unsolved",
        "timestamp":str(datetime.now())
        })

        res=db.grievance.find()
        for i in res:
            print('#\n\n\n\n\n\n',i)

        return 'db.grievance.find()'


@app.route('/records')
def records():
    db = app.data.driver.db.client['nibodh']
    all=db.grievance.find()

    for i in all:
        if 'area' not in i:
            lon=float(i.longitude)
            lat=float(i.latitude)
            tup=(lat,lon)
            res=reverseGeocode(tup)
            print('\n\n\nres:',res)
            i.update({"area"})

        '''print('\nuserid:',i.user_id)
        print('\nlongitude:',i.longitude)
        print('\nlatitude:',i.latitude)
        print('\ndate:',i.assigned_date)'''

    return render_template('tables.html',{'all':all})


@app.route('/bar')
def bar():
    pincode=[11,12,11,13,15,11,16,17]
    tmp=set(pincode)
    count=[]
    print(tmp)
    for i in tmp:
        print(pincode.count(i))
        count.append(pincode.count(i))
    tick_label = ['one', 'two', 'three', 'four', 'five','six']
    print(count)
    pincode=list(tmp)
    print(pincode)
    plt.bar(pincode,count, tick_label = tick_label,width = 0.8, color = ['red', 'green'])
    plt.xlabel('Problems')
    plt.ylabel('Area')
    plt.title('Pincode')
    #plt.savefig('/graphs'+str(datetime.now())+'.png')
    return 'hii'


@app.route("/smd")
def index():
    db = app.data.driver.db.client['nibodh']
    all=list(db.grievance.find())

    for i in all:
        if 'area' not in i:
            lon=float(i['longitude'])
            lat=float(i['latitude'])
            print('\n\n\n\n\nlon:',lon)
            tup=(lat,lon)
            print('\n\n\n\n\ntup:',tup)
            res=reverseGeocode(tup)
            i.update({"area":res})



    return render_template('edit.html',all=all)


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
