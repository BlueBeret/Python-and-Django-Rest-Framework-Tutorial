from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    class Meta:
        model = Todo
        fields = "__all__"