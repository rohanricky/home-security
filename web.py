import json
import os
import requests
from flask import Flask, request ,Response
import configparser
from intrusion import secret_cam

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
# send post request to my computer

if __name__=='__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT', 5000)), debug=True)
