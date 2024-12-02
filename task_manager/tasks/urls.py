from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, register_user


router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
]