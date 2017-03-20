from model.File import File
import requests
import json



class Delete_Service:


    def __init__(self,id):
    	#consult_data_base 
        try:
            self.document = File.get_doct(id)
            self.warning = ""
        except Exception as e:
            self.document = None
            self.warning = "Unexisting Document"

    def delete(self):
        #delete
        if self.document != None:
            File.delete_doct(self.document)
            return "",204
        else:
            return self.warning,404
