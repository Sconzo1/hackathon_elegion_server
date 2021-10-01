from rest_framework import serializers

from authentication.serializers import UserSerializer
from .models import Task
from .models import UserTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserTaskSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True, source='id_user')
    # task = TaskSerializer(read_only=True, source='id_task')
    # manager = UserSerializer(read_only=True, source='id_manager')

    class Meta:
        model = UserTask
        fields = '__all__'
