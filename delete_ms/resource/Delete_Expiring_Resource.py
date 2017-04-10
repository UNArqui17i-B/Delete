from service.Delete_Expiring_Service import Delete_Expiring_Service
from flask_restful import Api, Resource

class Delete_Expiring_Resource(Resource):

    def delete(self,exp_date):
        service = Delete_Expiring_Service(exp_date)
        response = service.delete_expiring()
        message = response[0]
        code = int(response[1])
        response = {"deleted":message}
        return response,code
