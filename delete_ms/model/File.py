from couchdb.mapping import Document, TextField, IntegerField, \
    DateTimeField, ListField, DecimalField
from datetime import datetime, timedelta, time


class File(Document):

    def __init__(obj):
        self._id = obj['_id']
        self._rev = obj['_rev']
        self.name = obj['name']
        self.extension = obj['extension']
        self.size = obj['size']
        self.uploaded_date = obj['uploaded_date']
        self.expiring_date = obj['expiring_date']
        self.owner_id = obj['owner_id']
        self.shared = obj['shared']

    _id = TextField()
    _rev = TextField()
    name = TextField()
    extension = TextField()
    size = IntegerField()

    # If the upload_date isn't given, upload_date will be the today date in seconds since the Epoch

    uploaded_date = DecimalField(default=time)

    # If the expiring_date isn't given, expiring_date will be today date in a week in seconds since the Epoch

    expiring_date = DecimalField()
    owner_id = TextField()
    shared = ListField(TextField())



			