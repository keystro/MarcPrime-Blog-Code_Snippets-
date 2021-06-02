#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import IPAddressType
import secrets, os
basedir = os.path.abspath(os.path.dirname(__file__))


app=Flask(__name__)
app.config['SECRET_KEY']='Hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data-drive.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

#db model

class Device(db.Model):
    __tablename__='device'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    device_name = db.Column(db.String(60), unique=False, nullable=False)
    device_ip = db.Column(IPAddressType, unique=True, nullable=False)
    api_token = db.Column(db.String(128), unique=True, nullable=False)

    #method to print out resutls of query without specifying object attribute
    def __repr__(self):
        return f"Device('{self.device_name}','{self.device_ip}','{self.api_token}')"


#application routes
@app.route('/')
@app.route('/index', methods=['POST','GET'])
def index():
    #get data from ESP
    package = request.get_json()
    ipaddr = package['ipaddr']
    name = package['name']
    token = secrets.token_hex(16)
    packet = Device(device_name=name, device_ip=ipaddr, api_token=token)
    db.session.add(packet)
    db.session.commit()
    return jsonify({'name':name, 'ipaddr':ipaddr, 'api_token': token})


if __name__=='__main__':
    app.run(debug=True, host='192.168.1.104', port=5000)



    