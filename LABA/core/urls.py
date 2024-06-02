from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import forms

app_name = 'core'


urlpatterns = [
    path('',views.index,name='index'),
    path('signin/', views.signin, name='signin'),    
    path('login/', auth_views.LoginView.as_view(authentication_form=forms.LoginForm,template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/',views.about,name='about'),
    
    path('view_orders/',views.view_orders,name='view_orders'),
    path('sales_info/',views.sales_info,name='sales_info'),
    path('statics/',views.statics,name='statics'),
    
    
    path('news/',views.news,name='news'),
    path('questions/',views.questions,name='questions'),
    path('contacts/',views.contacts,name='contacts'),
    path('terms/',views.terms,name='terms'),
    
    path('work/',views.work,name='work'),
    path('work/add_vacancy/',views.add_vacancy,name='add_vacancy'),
    path('update_vacancy/<int:vacancy_id>/', views.update_vacancy, name='update_vacancy'),
    path('delete_vacancy/<int:vacancy_id>/', views.delete_vacancy, name='delete_vacancy'),
    
    
    
    path('rewiews/',views.rewiews,name='rewiews'),
    path('add_comment/' , views.add_comment, name='add_comment'),
    path('coupons/',views.coupons,name='coupons'),
    
    path('show_time/',views.show_time,name='show_time'),
    
    path('search',views.search,name='search'),
    
]





