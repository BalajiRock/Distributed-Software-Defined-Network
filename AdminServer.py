from flask import Flask, Response, request ,jsonify
from flask_cors import CORS
import json
from flask import Flask
from flask_cors import CORS, cross_origin

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

global app
app = Flask(__name__)
CORS(app)
 
managerLeaderIP = "" 

def setManagerLeader(data):
    global managerLeaderIP
    managerLeaderIP = data
    return managerLeaderIP
def getManagerLeader():
    global managerLeaderIP
    return managerLeaderIP
 
@app.route("/GetManagerLeaderIP",methods =['POST'])
def SendManagerLeaderIP():
    data = {"leaderIP":getManagerLeader()}
    data = json.dumps(data)
    return data


# @app.route("/GetLeaderIPNode",methods =['POST'])
# def sendLeaderIP():
#     return getManagerLeader()


@app.route('/api/admin/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if username == 'a@a.com' and password == '123':
        token = 'login_done'
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
    



@app.route("/RequestOTP",methods =['GET'])
@cross_origin()
def SendOTP():
    otp = input("Enter Otp :")
    return jsonify(otp),200

@app.route("/HeartBeatFromManager",methods =['POST'])
def Updatemanager():
    req = request.data.decode()
    req = json.loads(req)
    setManagerLeader(req["leaderIP"])
    return ("alive")

app.run(debug=False,port=3000,host='127.0.1.1')