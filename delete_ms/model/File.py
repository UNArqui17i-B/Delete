from couchdb.mapping import Document, TextField, IntegerField, \
    DateTimeField, ListField, DecimalField
from datetime import datetime, timedelta, time
from couchdb import Server
from os import environ


host = environ["HOST_DATABASE"]
port = environ["HOST_DATABASE_PORT"]
database = environ["DATABASE_NAME"]
url = "http://{0}:{1}/".format(host,port)
server = Server(url=url)

class File(Document):

    @staticmethod
    def get_doct(id):
    	db = server[database]
        return db[str(id)]

    @staticmethod
    def delete_doct(deleted_file):
    	db = server[database]
        db.delete(deleted_file)



			