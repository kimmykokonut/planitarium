from rest_framework import serializers
from .models import Category, Tag, Task
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'