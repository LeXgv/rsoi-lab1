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
        self.assertEquals(c.post('/api/v1/users/', json.dumps({'name': 'Igor', 'age': 10}), content_type='text/json').content, b'ok')
        self.assertEquals(c.post('/api/v1/users/', json.dumps({'name': 'Olga', 'age': 16}), content_type='text/json').content, b'ok')
        self.assertEquals(c.post('/api/v1/users/', json.dumps({'name': 'Anton', 'age': 50}), content_type='text/json').content, b'ok')
        self.assertEquals(c.get('/api/v1/users/').content, b'[]')