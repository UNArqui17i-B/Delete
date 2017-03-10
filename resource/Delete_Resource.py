from service.Delete_Service import Delete_Service
from flask_restful import Api, Resource

class Delete_Resource(Resource):

    def delete(self,id):
        service = Delete_Service(id)
        response = service.delete()
        message = response[0]
        code = int(response[1])
        response = {"message":message}
        return object,code