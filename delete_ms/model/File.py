from couchdb.mapping import Document, TextField, IntegerField, \
    DateTimeField, ListField, DecimalField
from datetime import datetime, timedelta, time
from couchdb import Server
from os import environ


host = environ["DB_URL"]
port = environ["DB_PORT"]
database = environ["DB_NAME"]
#database = "blinkbox_files"
#host = "127.0.0.1"
#port = "5984"
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

    @staticmethod
    def get_expiring_docs(exp_date):
        ids = []
        db = server["blinkbox_files"]
        results = db.view('_design/exp_date/_view/get_by_exp_date',startkey=0, endkey=exp_date)
        for row in results:
            ids.append(row.id)
        return ids



			