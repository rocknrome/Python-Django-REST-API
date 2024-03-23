from .models import TodoItem
from rest_framework import serializers, permissions
from .serializers import TodoSerializer

class TodoItemSerializer(serializers.ModelSerializer):
   # for configuring the todoserializer above
    queryset = TodoItem.objects.all()
    # use the TodoSerializer class to serialize the data
    serializer_class = TodoSerializer
    # unrestricted access to the API
    permission_classes = [permissions.AllowAny]

    # no need to create routes. these are it.