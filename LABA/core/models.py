from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from datetime import date


class User(AbstractUser):
    date_of_birth = models.DateField('date_of_birth', null=True, blank=True)
    address = models.CharField('address', max_length=255, blank=True)
    number = models.CharField('phone number', max_length=20, blank=True)
    has_rewiews=models.BooleanField('has_rewiews', default=False)
    
    
    #groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year
            if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
                age -= 1
            return age
        return None




class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    position=models.CharField(max_length=200)
    salary=models.FloatField(null=False, blank=False)
    hire_date=models.DateField(null=False, blank=False)
    image=models.ImageField(upload_to='employee_images/',blank=True,null=True,default='employee_images/photo_2023-12-03_02-14-05.jpg')
    user_id=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user_id.username




class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    user_id=models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    image=models.ImageField(upload_to='employee_images/',blank=True,null=True,default='employee_images/photo_2023-12-03_02-14-05.jpg')
    salary=models.FloatField(null=False, blank=False,default=None)
    position=models.CharField(max_length=200,default='MAIN ADMIN')
    
    def __str__(self) -> str:
        return self.user_id.username





class Zakazchik(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE,default=None) 
    amount_zakazov=models.IntegerField(default=0)




