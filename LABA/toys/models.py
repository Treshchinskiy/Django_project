from django.db import models
from core.models import User, Zakazchik
from django.core.validators import MinValueValidator, MaxValueValidator
#промокоды еще нужны но там отдельная пизда



class Promocode(models.Model):
    id = models.AutoField(primary_key=True)
    percent_discount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    description = models.TextField()
    code=models.CharField(max_length=50)
    
    def __str__(self):
        return self.description
    
    def apply_discount(self, amount):
        discount_amount = amount * (self.percent_discount / 100)
        return amount - discount_amount
    
 
 
 
 
class News(models.Model):
    id = models.AutoField(primary_key=True)
    article=models.CharField(max_length=200)
    text=models.TextField()
    image=models.ImageField(upload_to='news_images/',blank=True,null=True,default='news_images/photo_2023-05-23_14-28-57.jpg')

    def __str__(self):
        return self.article
    
    
class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    proffesion = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    
    def __str__(self):
        return self.proffesion
    
    

class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    question=models.CharField(max_length=200)
    answer=models.TextField()
    date=models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.question



class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    description=models.TextField(default=None)

    def __str__(self):
        return self.name









class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    product_code = models.CharField(max_length=50)
    price=models.FloatField(null=False, blank=False)
    image=models.ImageField(upload_to='product_images/',blank=True,null=True,default='product_images/FCxARCPWYAEi9ux.jpg')
    status=models.CharField(max_length=100)
    product_type_id = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    amount=models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name




class Rewiews(models.Model):
    id = models.AutoField(primary_key=True)
    rewiew=models.CharField(max_length=1500)
    client_id=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField(null=True)
    stars = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5 stars"
    ,default=5)
    
    def __str__(self) -> str:
        return self.rewiew



class Sale(models.Model):
    id=models.AutoField(primary_key=True)
    order_date=models.DateField(null=False, blank=False)
    delivery_date=models.DateField(null=False, blank=False)
    quantity=models.IntegerField(null=False, blank=False,default=1)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    zakazchik_id=models.ForeignKey(Zakazchik,on_delete=models.CASCADE,default=None)
    promocode_id = models.ForeignKey(Promocode, on_delete=models.CASCADE, null=True, blank=True,default=None)
    promocode=models.CharField(max_length=100,default='')




