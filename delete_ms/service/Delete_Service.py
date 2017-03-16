from model.File import File
from couchdb import Server
import requests
import json

host = "192.168.99.101"
port = "3010"
url = "http://{0}:{1}/".format(host,port)
server = Server()

class Delete_Service:


    def __init__(self,id):
    	#consult_data_base
        db = server["file"]
        obj = requests.get('{0}file/_design/new_doc/_view/by_id?key="{1}"'.format(url,id))
        obj= json.loads(obj.text)
        if len(obj["rows"]) == 1:
            document = obj["rows"][0]["value"]
            document = db[document["_id"]]
            self.document = document
            self.warning = ""
        else:
            self.document = None
            self.warning = "Unexisting Document"

    def delete(self):
        #delete
        db = server["file"]
        if self.document != None:
            deleted_file = self.document
            db.delete(self.document)
            return "",204
        else:
            return self.warning,404
