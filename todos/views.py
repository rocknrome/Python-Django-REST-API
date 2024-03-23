from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    #Everything in the todo object (which is everything -everything)
    queryset=Todo.objects.all()
    # sepcificies the which serializer to use. In this case, we will be use the file: TodoSerializer to do the serialization and deserialization
    serializer_class=TodoSerializer
    # unrestricted access to the api
    permission_classes=[permissions.AllowAny]