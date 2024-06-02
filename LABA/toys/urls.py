from django.urls import path
from django.contrib.auth import views as auth_views
from .views import news_detail,create_toy,create_toy_detail,order

app_name = 'toys'


urlpatterns = [
    path('news/<int:id>/', news_detail, name='news_detail'),
    path('create/', create_toy, name='create_toy'),
    path('create/<int:id>/',create_toy_detail,name='create_toy_detail'),
    path('order/',order,name='order'),
 
]