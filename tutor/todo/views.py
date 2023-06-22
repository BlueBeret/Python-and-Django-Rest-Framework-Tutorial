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

    def get_queryset(self):
        todos = Todo.objects.all().order_by('-id')
        return todos
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = TodoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            new_todo = Todo.objects.create(**serializer.validated_data)
            new_todo.save()
            return Response("object created", status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = TodoSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
