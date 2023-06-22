from django.shortcuts import render
from rest_framework import viewsets
from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class TodoViewsets(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    methods = ['GET','PUT', 'POST', 'DELETE']

    # create your own api