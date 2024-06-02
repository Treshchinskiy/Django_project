from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TextRequest,Test
from .serializer import TextRequestSerializer,TestSerializer
import requests
from django.http import JsonResponse
import json

#google-t5/t5-small
#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 - token

class HuggingFaceAPIView(APIView):  
    def post(self, request):
        input_text = request.POST.get('input-text', '')

        api_url = "https://api-inference.huggingface.co/models/t5-small"


        api_token = "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"
        headers = {
            "Authorization": f"Bearer {api_token}"
        }

        data = {
            "inputs": input_text
        }

        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            transformed_text = result[0]['translation_text']
        else:
            print(response.status_code)
            transformed_text = "Error: Unable to process the text."

        return render(request, 'api/translator.html', {
            'input_text': input_text,
            'transformed_text': transformed_text
        })


    def get(self, request):
        return render(request, 'api/translator.html')





#return Response({'post': WomanSerializer(lst, many=True)  })
class TestApi(APIView):

    def get(self, request):
        response = requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist')
        try:
            json_data = response.json()
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            print("Response content:", response.content)
            json_data = None
            
        if json_data['type']  == 'twopart':
            setup=json_data['setup']
            delivery=json_data['delivery']
            return render(request, 'api/second_api.html', {'setup': setup,'delivery':delivery})
        else:
            return render(request, 'api/second_api.html', {'json_data': json_data['joke']})    
        
            
    



