from django.test import TestCase
from ..models import Category, Tag, Task
from ..serializers import CategorySerializer, TagSerializer, TaskSerializer
from django.contrib.auth.models import User
import datetime

class CategorySerializerTest(TestCase):
    def setUp(self):
        self.category_data = {'label': 'Work'}
        self.category = Category.objects.create(**self.category_data)
        self.serializer = CategorySerializer(instance=self.category)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'label']))

    def test_label_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['label'], self.category_data['label'])

class TagSerializerTest(TestCase):
    def setUp(self):
        self.tag_data = {'label': 'Urgent'}
        self.tag = Tag.objects.create(**self.tag_data)
        self.serializer = TagSerializer(instance=self.tag)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'label']))

    def test_label_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['label'], self.tag_data['label'])

class TaskSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='kiko', password='password')
        self.category = Category.objects.create(label="Work")
        self.tag = Tag.objects.create(label="Urgent")
        self.task_data = {
            'name': 'Test Task',
            'description': 'This is a test task',
            'start_time': datetime.time(9, 0),
            'end_time': datetime.time(10, 0),
            'day_of_week': 0,
            'location': 'Home',
            'category': self.category.id,
            'tags': [self.tag.id],
            'priority': 2,
            'status': 'P',
            'is_recurring': False,
            'user': self.user.id
        }
        self.task = Task.objects.create(
            name='Test Task',
            description='This is a test task',
            start_time=datetime.time(9, 0),
            end_time=datetime.time(10, 0),
            day_of_week=0,
            location='Home',
            category=self.category,
            priority=2,
            status='P',
            is_recurring=False,
            user=self.user
        )
        self.task.tags.add(self.tag)
        self.serializer = TaskSerializer(instance=self.task)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set([
            'id', 'name', 'description', 'start_time', 'end_time', 'day_of_week',
            'location', 'category', 'tags', 'priority', 'status', 'is_recurring', 'user'
        ]))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.task_data['name'])

    def test_category_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['category'], self.category.id)

    def test_tags_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['tags'], [self.tag.id])