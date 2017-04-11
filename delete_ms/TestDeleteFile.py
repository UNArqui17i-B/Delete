from couchdb import Server
import delete_app
import unittest
import requests
import json

host = '127.0.0.1'
port = '5984'
database = 'blinkbox_files'
url = 'http://{0}:{1}/'.format(host, port)
server = Server(url=url)


class TestDeleteFile(unittest.TestCase):

    def setUp(self):
        self.app = delete_app.app.test_client()

    def test_is_running(self):
        response = self.app.get('/')
        self.assertEqual(response.get_data(), 'Hello DOCKER & Delete')

    def test_delete_file(self):
        id = 'No_One_Ever_Will_Use_This_Id'
        doc = {
            '_id': id,
            'name': 'Mi Documento',
            'extension': '.algo',
            'size': 123,
            'upload_date': 1489947657,
            'expiring_date': 1490811657,
            'owner_id': 'my_id',
            'shared': ['one@gmail.com', 'two@gmail.com'],
            }
        db = server[database]
        db.save(doc)
        response = self.app.delete('/delete/file/' + str(id))
        assert response.status_code == 204
        assert id not in db


if __name__ == '__main__':
    unittest.main()


				