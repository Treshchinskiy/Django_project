from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .models import Women
from .serializer import WomanSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class WomenApiView(APIView):
    def get(self,request): #отвечает за обработку get запросов
        lst = Women.objects.all().values()
            
        return Response({'post': WomanSerializer(lst, many=True)  })
    
    
    def post(self,request):
        post_new=Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})
    
    

""" class WomenApiView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomanSerializer
 """