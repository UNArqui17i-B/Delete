from model.File import File
from service.Delete_Service import Delete_Service
import requests
import json



class Delete_Expiring_Service:


    def __init__(self,exp_date):
    	#consult_data_base 
        self.ids = File.get_expiring_docs(exp_date)

    def delete_expiring(self):
        #delete
        for id in self.ids:
        	service = Delete_Service(id)
        	service.delete()
        return self.ids,202
