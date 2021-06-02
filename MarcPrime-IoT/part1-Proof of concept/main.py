#!/usr/bin/python3
#!/usr/flask/python3

from flask import Flask, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
#GET REQUEST
@app.route("/")
@app.route("/main")
def main():
    return "Hello! World, Connection to MarcPrime IoT Successful"

#GET REQUEST with JSON RESPONSE
#GET REQUEST with JSONIFY
@app.route("/index")
def index():
    return jsonify ({'Name':'MarcPrime IoT',
                     'IP':'192.168.1.XXX',
                     'Message':'**** Hello! World, ****',
                     'Message1':'**** Connection to IoT Device is Successful ****'})

#POST REQUEST with JSON
@app.route("/posturl", methods = ['POST','GET'])
def posturl():
    data = request.get_json()
    print(data)

    name = data['name']
    ipadr = data['ipadr']
    message = data['message']
    message1 = data['message1']
    temp = data['temp']
    watts = data['watts']

    if temp >= 40:
        return '1'
    elif temp < 40 :
        return '0'
    else: 
        return None
    #return jsonify({"Message":"Json Data Recieved"})



if __name__=="__main__":
    app.run(debug=True, host='192.168.1.104', port=8091)