from couchdb.mapping import Document, TextField, IntegerField, DateTimeField
from datetime import datetime,timedelta
class File(Document):

	_id = IntegerField()
	name = TextField()
	extension = TextField()
	uploaded_date = DateTimeField(default = datetime.now())
	expiring_date = DateTimeField(default = datetime.now() + timedelta(days=7))
	owner_id = IntegerField()
