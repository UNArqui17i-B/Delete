from model.File import File
from couchdb import Server

db = server["File"]

class Delete_Service():

    def __init__(self,id):
    	#consult_data_base
    	#file = File.load(db, id)
    	#if file != None
        self.delete_file = a_file

    def delete(self):
        deleted_file = self.delete_file()
        db.delete(deleted_file)
        return "",204
