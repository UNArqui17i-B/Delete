from model.File import File
import requests
import json



class Get_Service:


    def __init__(self,exp_date):
    	#consult_data_base 
        self.ids = File.get_expiring_docs(exp_date)

    def get(self):
        #get
        return self.ids,202
