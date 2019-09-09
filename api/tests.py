import django.test
from django.test import Client
import json
import api

class view_users_test(django.test.TestCase):
    '''def test_view(self):
    request = HttpRequest()
    request.method = "GET"
    response = views.users(request)
    self.assertEquals(response.content, b'[]')
    request.GET = '''

    def test_add_and_get_users(self):
        c = Client()
        self.assertEquals(c.get('/api/v1/users/').content, b'[]')
        self.assertEquals(
            c.post('/api/v1/users/', json.dumps({'name': 'Igor', 'age': 10}),
                   content_type='text/json').content,b'ok')
        self.assertEquals(c.post('/api/v1/users/', json.dumps({'name': 'Olga', 'age': 50}),
                                 content_type='text/json').content, b'ok')
        self.assertEquals(c.post('/api/v1/users/', json.dumps({'name': 'Anton', 'age': 50}),
                                 content_type='text/json').content, b'ok')
        self.assertEquals(c.get('/api/v1/users/').content,
                          b'[{"type": "dbPerson", "id": 1, "name": "Igor", "age": 10},'
                          b'{"type": "dbPerson", "id": 2, "name": "Olga", "age": 50},'
                          b'{"type": "dbPerson", "id": 3, "name": "Anton", "age": 50}]')
        self.assertEquals(c.post('/api/v1/users/', json.dumps({'name': 'Anton'}),
                                 content_type='text/json').content,
                          b'{"type": "error", "id": 4, "info": "Wrong json object."}')
        self.assertEquals(c.get('/api/v1/users/?age=50', content_type='text/json').content,
                          b'[{"type": "dbPerson", "id": 2, "name": "Olga", "age": 50},'
                          b'{"type": "dbPerson", "id": 3, "name": "Anton", "age": 50}]')
        self.assertEquals(c.get('/api/v1/users/?age=51', content_type='text/json').content,
                          b'{"type": "error", "id": 2, "info": "Object does not exist"}')
        self.assertEquals(c.get('/api/v1/users/?ge=51', content_type='text/json').content,
                          b'{"type": "error", "id": 3, "info": "wrong argument"}')
        self.assertEquals(c.get('/api/v1/users/?age=50&name=Olga', content_type='text/json').content,
                          b'{"type": "error", "id": 1, "info": "You sent in request type get more then one argument"}')

