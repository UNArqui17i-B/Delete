from couchdb.mapping import Document, TextField, IntegerField, DateTimeField,ListField
from datetime import datetime,timedelta
class File(Document):

	_id = TextField()
	name = TextField()
	size = IntegerField()
	extension = TextField()
	uploaded_date = DateTimeField(default = datetime.now())
	expiring_date = DateTimeField(default = datetime.now() + timedelta(days=7))
	owner= TextField()
	emails = ListField(TextField)
	attachment = Document()
