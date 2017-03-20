from couchdb.mapping import Document, TextField, IntegerField, \
    DateTimeField, ListField, DecimalField
from datetime import datetime, timedelta, time
from couchdb import Server


host = "192.168.99.101"
port = "3010"
url = "http://{0}:{1}/".format(host,port)
server = Server(url=url)
db = server["file"]

class File(Document):

    @staticmethod
    def get_doct(id):
        return db[str(id)]

    @staticmethod
    def delete_doct(deleted_file):
        db.delete(deleted_file)



			