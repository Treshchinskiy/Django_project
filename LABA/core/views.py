from django.shortcuts import render,redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from core.models import User,Zakazchik
from toys.models import News, Questions, Vacancy, Product, Rewiews,Sale,Promocode
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Employee
from .forms import RewiewsForm,VacancyForm
from django.http import HttpResponse
import logging
from collections import namedtuple
import matplotlib.pyplot as plt
from django.conf import settings
import os
from django.db.models import Count


logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')

User = get_user_model()


def signin(request):
    if request.method == 'POST':  
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)
           
            logging.info(f"SIGN IN IS COMPLETED")
             
            return redirect("/") 
        
        else:
            for error in form.errors.values():
                messages.error(request, error) 
    else: 
        form = SignupForm()

    logging.info(f"SIGN IN FORM WAS REQUIRED")

    return render(request, 'core/signin.html', {'form': form})




def index(request):
    
    items=Product.objects.all().order_by('price')
    last_news = News.objects.last()
    logging.info("MAIN PAGE WAS REQUIRED")
    
    return render(request,'core/index.html',{'items':items,'last_news':last_news,'request':request})




def about(request):
    logging.info(f"SOMEONE IS READING ABOUT OUT COMPANY")
    
    return render(request,'core/about.html')
    
    
    
def contacts(request):
    Workers=Employee.objects.all()
    
    return render(request,'core/contacts.html',{'Workers':Workers})



def coupons(request):
    discounts=Promocode.objects.all()
    return render(request,'core/coupons.html',{'discounts':discounts})
        
        
def news(request):
    news_list=News.objects.all()
    
    return render(request,'core/news.html',{'news_list':news_list})
    
    
def questions(request):
    All_questions=Questions.objects.all()
    
    return render(request,'core/questions.html',{'All_questions':All_questions})
    
    
def rewiews(request):
    reviews=Rewiews.objects.all()
    
    
    return render(request,'core/rewiews.html',{'reviews':reviews, 'request':request})
    
    
def add_comment(request):
    if request.method == 'POST':
        form=RewiewsForm(request.POST)
        if form.is_valid():
            
            old_comment = Rewiews.objects.filter(client_id=request.user).first()
            if old_comment:
                old_comment.delete() 
                 
            item=form.save(commit=False)
            item.client_id=request.user
            item.save()
            request.user.has_rewiews = True
            request.user.save()
            return redirect('/rewiews')
        
    else:
        form=RewiewsForm()
    
    return render(request, 'core/add_comment.html', {'form': form})
    
    
    
    
def terms(request):
    return render(request,'core/terms.html')



def work(request):
    Works=Vacancy.objects.all()
    
    
    return render(request,'core/work.html',{'Works':Works,'request':request})
    
    
    
    
    
def view_orders(request):
    user = request.user
    try:
        zakazchik = Zakazchik.objects.get(user=user)
    except Zakazchik.DoesNotExist:
        return HttpResponse("No orders found for this user.", status=404)
    orders = Sale.objects.filter(zakazchik_id=zakazchik)
    orders_with_total = []
    for order in orders:
        total_price = order.quantity * order.product_id.price
        if order.promocode == '1010':
            total_price *= 0.9
        if order.promocode == '5050':
            total_price *= 0.95
        orders_with_total.append({
            'order': order,
            'total_price': total_price
        })
    return render(request, 'core/view_orders.html', {'orders_with_total': orders_with_total})




def add_vacancy(request):
    if request.method == 'POST':
        form=VacancyForm(request.POST)
        if form.is_valid():
            item=form.save(commit=False)
            item.save()
            return redirect('/work')
        
    else:    
        form=VacancyForm(request.POST)
    return render(request,'core/add_vacancy.html',{'form':form})
    


def update_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('/work')  # Перенаправление на домашнюю страницу после успешного обновления
    else:
        form = VacancyForm(instance=vacancy)
    
    return render(request, 'core/add_vacancy.html', {'form': form})




def delete_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    print(vacancy.proffesion)
    vacancy.delete()  
    return redirect('/work') 


import matplotlib
matplotlib.use('Agg')  

def build_distribution():
    sales = Sale.objects.all()
    sales_dict = {}
    for sale in sales:
        if sale.product_id.name in sales_dict:
            sales_dict[sale.product_id.name] += sale.quantity
        else:
            sales_dict[sale.product_id.name] = sale.quantity


    products = list(sales_dict.keys())
    quantities = list(sales_dict.values())

    plt.figure(figsize=(10, 6))
    plt.bar(products, quantities, color='blue')
    plt.xlabel('Products')
    plt.ylabel('Quantity Sold')
    plt.title('Distribution of Products Sold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    img_path = os.path.join(settings.MEDIA_ROOT, 'sales_distribution.png')
    plt.savefig(img_path)  
    plt.close()  

    return sales_dict, img_path
   
   
   
def sales_info(request):
    users_with_zakazi = User.objects.filter(zakazchik__isnull=False)
    
    UserInfo = namedtuple('UserInfo', ['user', 'orders', 'total_sum'])
    user_info_list = []
    
    for user in users_with_zakazi:
        user_orders = user.zakazchik.sale_set.all()
        
        total_sum = sum(order.quantity * order.product_id.price for order in user_orders)
        orders = list(set(order.product_id.name for order in user_orders))
        
        user_info_list.append(UserInfo(user=user, orders=orders, total_sum=total_sum))
    
    sales_dict, img_path = build_distribution()

    img_url = os.path.join(settings.MEDIA_URL, 'sales_distribution.png')

    return render(request, 'core/sales_info.html', {'user_info_list': user_info_list,'img_url': img_url})

    



def build_review_distribution():
    users_with_reviews = User.objects.filter(has_rewiews=True).count()
    users_without_reviews = User.objects.filter(has_rewiews=False).count()

    labels = ['Has Reviews', 'No Reviews']
    sizes = [users_with_reviews, users_without_reviews]
    colors = ['green', 'red']
    explode = (0.1, 0)  # немного сместим первый сегмент для акцента

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # равные оси, чтобы круг был кругом
    plt.title('Distribution of Users by Reviews')

    img_path = os.path.join(settings.MEDIA_ROOT, 'review_distribution.png')
    plt.savefig(img_path)
    plt.close()

    return {'has_reviews': users_with_reviews, 'no_reviews': users_without_reviews}, img_path


def build_star_distribution():
    star_counts = Rewiews.objects.values('stars').annotate(count=Count('stars')).order_by('stars')

    stars = [entry['stars'] for entry in star_counts]
    counts = [entry['count'] for entry in star_counts]

    plt.figure(figsize=(10, 6))
    plt.bar(stars, counts, color='blue')
    plt.xlabel('Stars')
    plt.ylabel('Number of Reviews')
    plt.title('Distribution of Reviews by Star Rating')
    plt.xticks(stars)  
    plt.tight_layout()

    # Сохранение диаграммы
    img_path = os.path.join(settings.MEDIA_ROOT, 'star_distribution.png')
    plt.savefig(img_path)
    plt.close()

    return dict(zip(stars, counts)), img_path



def statics(request):
    from django.db.models import Avg
    users_with_age = User.objects.exclude(date_of_birth__isnull=True)
    average_age = [user.age for user in users_with_age if user.age is not None]
    average_age=sum(average_age)/len(average_age)
    
    a,img_path = build_review_distribution()

    img_url = os.path.join(settings.MEDIA_URL, 'review_distribution.png')
    
    b,img_path2=build_star_distribution()
    img_url2 = os.path.join(settings.MEDIA_URL, 'star_distribution.png')
    
    
    return render(request,'core/statics.html', {'average_age': average_age, 'img_url': img_url, 'img_url2': img_url2})




def search(request):
    query = request.GET.get('q')
    
    items = Product.objects.filter(name=query)
    last_news = News.objects.last()
    
    return render(request,'core/index.html',{'last_news':last_news,'request':request,'items':items})







import pytz
from django.utils import timezone

def show_time(request):
    if request.method == 'POST':
        user_timezone = request.POST.get('timezone')
        current_time = timezone.now()
        user_time = current_time.astimezone(pytz.timezone(user_timezone))
        return render(request, 'core/show_time.html', {'user_time': user_time})

