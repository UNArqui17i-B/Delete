from couchdb.mapping import Document, TextField, IntegerField, DateTimeField
from datetime import datetime
class File(Document):

	id = IntegerField()
	name = TextField()
	extension = TextField()
	uploaded_date = DateTimeField(default = datetime.now)
	expiring_date = DateTimeField(default = datetime.now + datetime.timedelta(days=7))
	owner_id = IntegerField()
	