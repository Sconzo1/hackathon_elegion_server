from django.utils.decorators import method_decorator
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, permissions

from validators import validate_int
from . import serializers
from .models import Task
from .models import UserTask


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer


@method_decorator(name='list',
                  decorator=extend_schema(parameters=[OpenApiParameter(name='id_user', type=OpenApiTypes.INT)]))
class UserTaskView(viewsets.ModelViewSet):
    queryset = UserTask.objects.all()
    serializer_class = serializers.UserTaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    filter_fields = ['id_user']

