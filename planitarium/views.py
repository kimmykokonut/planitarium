from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Tag, Task
from .serializers import CategorySerializer, TagSerializer, TaskSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

def index(request):
  return HttpResponse("You are at the index page!")

class CategoryViewSet(viewsets.ModelViewSet):
  #ModelViewSet dRF has Crud under the hood. specify model/serializer
  queryset = Category.objects.all().order_by('label')
  serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all().order_by('label')
  serializer_class = TagSerializer

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all().order_by('name')
  serializer_class = TaskSerializer