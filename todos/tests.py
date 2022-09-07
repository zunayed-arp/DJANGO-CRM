from django.test import TestCase

from .models import Todo

class TestModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(title="First Todo",body="A body of test of first todo")
        
        
    def test_model_content(self):
        self.assertEqual(self.todo,"First Todo")
        self.assertEqual(self.todo.body,"A body of test of first todo")
        self.assertEqual(str(self.todo),"First Todo")