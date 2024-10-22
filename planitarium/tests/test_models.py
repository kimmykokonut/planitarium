from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Category, Tag, Task
from django.core.exceptions import ValidationError
import datetime

class CategoryModelTest(TestCase):
    def test_string_representation(self):
        category = Category(label="Work")
        self.assertEqual(str(category), category.label)

class TagModelTest(TestCase):
    def test_string_representation(self):
        tag = Tag(label="Urgent")
        self.assertEqual(str(tag), tag.label)

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Test User", password="password")
        self.category = Category.objects.create(label="Work")
        self.tag = Tag.objects.create(label="Urgent")
        self.task = Task.objects.create(
            name="Test Task",
            description="This is a test task",
            start_time=datetime.time(9, 0),
            end_time=datetime.time(10, 0),
            day_of_week=0,
            location="Home",
            category=self.category,
            priority=2,
            status='P',
            is_recurring=False,
            user=self.user
        )
        self.task.tags.add(self.tag)

    def test_string_representation(self):
        self.assertEqual(str(self.task), self.task.name)

    def test_end_time_after_start_time(self):
        self.task.end_time = datetime.time(8, 0)
        with self.assertRaises(ValidationError):
            self.task.clean()

    def test_invalid_day_of_week(self):
        self.task.day_of_week = 7
        with self.assertRaises(ValidationError):
            self.task.clean()

    def test_valid_task(self):
        try:
            self.task.clean()
        except ValidationError:
            self.fail("Task.clean() raised ValidationError unexpectedly!")