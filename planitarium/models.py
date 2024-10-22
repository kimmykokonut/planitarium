from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

class Category(models.Model):
  label = models.CharField(max_length=200)

  def __str__(self):
    return self.label
    
class Tag(models.Model):
  label = models.CharField(max_length=200)

  def __str__(self):
    return self.label

class Task(models.Model):
  PRIORITY_CHOICES = [
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High'),
  ]
  STATUS_CHOICES = [
    ('P', 'Pending'),
    ('C', 'Completed'),
    ('I', 'In Progress'),
  ]

  name = models.CharField(max_length=200)
  description = models.CharField(max_length=500)
  start_time = models.TimeField("Start Time", default=datetime.time(9,0))
  end_time = models.TimeField("End Time", default=datetime.time(10,0))
  day_of_week = models.IntegerField() #0 = Monday
  location = models.CharField(max_length=200, default="Home")
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag)
  priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
  status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
  is_recurring = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def clean(self):
    if not self.name:
      raise ValidationError('Name cannot be empty')
    if self.end_time <= self.start_time:
      raise ValidationError('End time must be after start time')
    if self.day_of_week not in range(7):
      raise ValidationError('Invalid day of the week')

  def __str__(self):
    return str(self.name)