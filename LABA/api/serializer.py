from .models import TextRequest,Test
from rest_framework import serializers




class TextRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextRequest
        fields = '__all__'
        
        
        
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Test
        fields='__all__'