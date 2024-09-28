from django.shortcuts import render, get_object_or_404, redirect
from .models import News,Product,Sale,Korzina
from .forms import ProductForm,ToyOrderForm
from core.models import Zakazchik
from django.utils import timezone
from datetime import timedelta

def news_detail(request, id):
    news = get_object_or_404(News, pk=id)
    return render(request, 'toys/news_detail.html', {'news': news})




def create_toy(request):
    if request.method == 'POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.client_id = request.user
            item.save()
            return redirect('/')
        
    else:
        form=ProductForm()
    
    return render(request, 'toys/create_item.html', {'form': form})
    
    
    
def create_toy_detail(request, id):
    toy=get_object_or_404(Product,pk=id)
    return render(request, 'toys/toys_detail.html',{'toy':toy,'request':request})


from django.core.exceptions import ValidationError
def order(request):
    if request.method == 'POST':
        form = ToyOrderForm(request.POST)
        if form.is_valid():
            number_of_toys = form.cleaned_data['number_of_toys']
            toy = form.cleaned_data['toy']
            promocode1 = form.cleaned_data['promocode']
            
            if toy.amount < number_of_toys:
                form.add_error('number_of_toys', f'There are only {toy.amount} units of {toy.name} available.')
                return render(request, 'toys/order_form.html', {'form': form})
            
            if promocode1:
                if promocode1 == '1010':
                    try:
                        z = Zakazchik.objects.get(user=request.user)
                    except Zakazchik.DoesNotExist:
                       pass
                    else:
                        z = None
                        form.add_error('promocode', 'It\'s not your first order')
                        return render(request, 'toys/order_form.html', {'form': form})
                elif promocode1 == '5050':
                    if number_of_toys * toy.price < 1000:
                        form.add_error('promocode', 'Your order must be at least for 1000$ for this promocode')
                        return render(request, 'toys/order_form.html', {'form': form})
                else:
                    form.add_error('promocode', 'There are no such promocode')
                    return render(request, 'toys/order_form.html', {'form': form})
                    
            z, created = Zakazchik.objects.get_or_create(user=request.user)    
            #z.amount_zakazov += 1
            z.save()
            

            #q = Sale(product_id=toy, quantity=number_of_toys, zakazchik_id=z, order_date=timezone.now(), delivery_date=timezone.now()+timedelta(weeks=1), promocode=promocode1)
            q=Korzina(product_id=toy, quantity=number_of_toys,user_id=request.user)
            q.save()
                        
            toy.amount -= number_of_toys
            toy.save()
            

            return redirect('/')
    else:
        form = ToyOrderForm()
    
    return render(request, 'toys/order_form.html', {'form': form})


