# encoding:utf-8

from flask import Flask, request
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('a', location='json')
parser.add_argument('b', location='json')


class Caculator_Add(Resource):
    def post(self):
        args = parser.parse_args()
        return int(args['a'])+int(args['b'])


api.add_resource(Caculator_Add, '/add')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8891, debug=True)
