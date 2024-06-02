from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from .models import News, Product, Zakazchik, Sale
from .forms import ProductForm, ToyOrderForm

User = get_user_model()


class NewsDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.news = News.objects.create(title='Test News', content='Test Content')

    


class OrderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
        self.toy = Product.objects.create(name='Test Toy', description='Test Description', price=10.0, amount=5, client_id=self.user)
        self.zakazchik = Zakazchik.objects.create(user=self.user, amount_zakazov=0)

   
   






