import json
import os
import requests
from flask import Flask, request ,Response
import configparser
from intrusion import secret_cam

config = configparser.ConfigParser()
config.read('config.ini')
access_token=config['HOST']
print(access_token['safety_token'])

app = Flask(__name__)


@app.route('/home')
def home():
    secret_cam()

if __name__=='__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
