# encoding:utf-8

from flask import Flask, request
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('a')
parser.add_argument('testkey', type=dict)     # !!! type dict 不能带引号
# parser.add_argument('b')
# parser.add_argument('c')


class Caculator_Add(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        # return
        return int(args['a']) + int(args['testkey']['b'])    # 字典取值后面没有点！！


api.add_resource(Caculator_Add, '/add')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8891, debug=True)
