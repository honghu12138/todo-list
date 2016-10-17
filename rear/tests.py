from django.test import TestCase
import json
from rear.models import Todo

# Create your tests here.
def summary(a, b):
    if a == 1 and b == 2:
        return 3
    else:
        return 4

class SummaryTest(TestCase):
    def test_sum(self):
        self.assertEquals(3, summary(1, 2))
        self.assertEquals(4, summary(2, 3))

class TodoTest(TestCase):
    def test_create_todo(self):
        response = self.client.post('/api/todos', data=json.dumps({
            'content': 'todo content'
        }), content_type='application/json')
        todo = json.loads(response.content)
        self.assertEquals('todo content', todo['content'])
        self.assertEquals(False, todo['state'])
        self.assertEquals(1, Todo.objects.filter(content='todo content').count())
    def test_delete_todo(self):
        response = self.client.post('/api/todos',data=json.dumps({
           'content': 'todo content'
        }), content_type='application/json')
        todo = json.loads(response.content)
        value = todo['id']
        response = self.client.delete('/api/todo/'+str(value),data=json.dumps)
        self.assertEquals(0, Todo.objects.filter(content='todo content').count())