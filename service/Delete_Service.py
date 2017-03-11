from model.File import File
from couchdb import Server
import requests
import json


class Delete_Service():

    def __init__(self,_id):
    	#consult_data_base

        server = Server()
        db = server["file"]
        obj = requests.get('http://127.0.0.1:5984/file/_design/new_doc/_view/by_id?key="{0}"'.format(_id))
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
        server = Server()
        db = server["file"]
        if self.document != None:
            deleted_file = self.document
            db.delete(self.document)
            return "",204
        else:
            return self.warning,404
