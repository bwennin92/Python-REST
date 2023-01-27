from sanic import Sanic
from sanic.response import text
from sanic_ext import Extend
from sanic_restful_api import Resource, Api

app = Sanic(__name__)
api = Api(app)
Extend(app)


class HelloWorld(Resource):
    async def get(self, request):
        return {'name':request.args.get ('name')}
    async def post(self,request):
        return request.form
api.add_resource(HelloWorld, '/')
