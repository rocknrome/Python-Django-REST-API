from .models import Todo
from rest_framework import serializers

# serializing and deserializing data (and data is the data from the table) to json
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # for configuring the todoserializer above
    class Meta:
            #model to serialize
            model=Todo
            #fields to show
            field=('id', 'subject', 'details')