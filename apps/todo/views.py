from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response

from apps.todo.models import ToDo
from apps.todo.serializers import ToDoSerializer

class ToDoAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     ):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

def perform_create(self, serializer):
        return serializer.save(user=self.request.user)