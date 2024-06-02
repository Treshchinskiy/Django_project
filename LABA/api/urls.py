from django.urls import path
from api.views import HuggingFaceAPIView, TestApi

app_name = 'api'

urlpatterns = [
    path('translator/', HuggingFaceAPIView.as_view() ,name='HuggingFaceAPIView'),
    path('second_api/',TestApi.as_view() ,name='TestApi'),

]



