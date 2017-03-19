from model.File import File
from couchdb import Server
import requests
import json

host = "192.168.99.101"
port = "3010"
url = "http://{0}:{1}/".format(host,port)
server = Server(url=url)

class Delete_Service:


    def __init__(self,id):
    	#consult_data_base
        db = server["file"]
        try:
            obj= db[str(id)]
            self.document = obj
            self.warning = ""
        except:
            self.document = None
            self.warning = "Unexisting Document"

    def delete(self):
        #delete
        db = server["file"]
        if self.document != None:
            deleted_file = self.document
            db.delete(deleted_file)
            return "",204
        else:
            return self.warning,404
