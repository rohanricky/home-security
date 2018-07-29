import json
import os
import requests
from flask import Flask, request ,Response
import configparser
from security_cam.intrusion import secret_cam

config = configparser.ConfigParser()
config.read('config.ini')
access_token=config['HOST']

app = Flask(__name__)


@app.route('/home')
def home():
    try:
        secret_cam()
    except ValueError:
        return "Fuck"

# @app.route('/cool',methods=['GET','POST'])
# def cool():
#     if request.method == 'POST':
#         return 'Damn it'
#     else:
#         return 'It damn'

# send post request to my computer

if __name__=='__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT', 5000)), debug=True)
