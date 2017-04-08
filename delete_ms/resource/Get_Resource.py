from service.Get_Service import Get_Service
from flask_restful import Api, Resource

class Get_Resource(Resource):

    def get(self,exp_date):
        service = Get_Service(exp_date)
        response = service.get()
        message = response[0]
        code = int(response[1])
        response = {"expired":message}
        return response,code
