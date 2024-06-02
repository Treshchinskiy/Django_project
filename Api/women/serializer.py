from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer




class WomanSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=255)
    content=serializers.CharField()
    time_create=serializers.DateTimeField()
    time_update=serializers.DateTimeField()
    is_published=serializers.BooleanField(default=True)
    cat_id=serializers.IntegerField()
    
    
    



    