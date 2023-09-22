from rest_framework.routers import DefaultRouter
from django.urls import path, include
from apps.todo.views import ToDoAPIViewSet

router = DefaultRouter()
router.register('todo', ToDoAPIViewSet, 'api_todo')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls 
