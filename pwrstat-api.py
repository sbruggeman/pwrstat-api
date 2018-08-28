#!/usr/bin/env python3

from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import subprocess

app = Flask(__name__)
api = Api(app)

class pwrstat(Resource):
    def get(self):
        status = subprocess.Popen(['pwrstat', '-status'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
        statusArr=[]
        statusDict={}

        for line in status.splitlines():
            line = line.lstrip()
            line = line.replace(". ",";")
            line = line.replace(".","")
            line = line.split(";")
            if len(line) > 1:
                statusArr.append(line)

        statusDict = {k[0]: k[1] for k in statusArr}

        return jsonify(statusDict)

api.add_resource(pwrstat, '/pwrstat') # return all parameters

if __name__ == '__main__':
     app.run(port=5002, host='0.0.0.0')