from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet, TaskViewSet

router = DefaultRouter()
# register vsets w router, endpoints auto generated
router.register(r'catgories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]