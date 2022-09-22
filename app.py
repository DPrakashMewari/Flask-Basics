import flask
from flask import Flask,request
import flask_restful
from flask_restful import Resource,Api
import json
app = Flask(__name__)

api = Api(app)

Data = []

class Prakash(Resource):
    def get(self,name):
        for x in Data:
            if x['Data'] == name:
                return x 
            return {'Data' :None}

    def post(self,name):
        Tem = {'Data':name}
        Data.append(Tem)
        return Tem

    def delete(self,name):
        for ind,x in enumerate(Data):
            if x['Data'] == name:
                Tem = Data.pop(ind)
                return {'Note':'Deleted'}

api.add_resource(Prakash,'/Name/<string:name>')
if __name__ == "__main__":
    app.run(debug=True)
