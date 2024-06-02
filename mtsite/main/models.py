from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#или можно проверять через панель администратора
#проверять содержимое бд как я понял можно только через консоль
#python manage.py shell

'''
from main.models import Item, ToDoList

In [2]: t=ToDoList(name="Tims List")

In [3]: t.save()

In [4]: ToDoList.objects.all()
Out[4]: <QuerySet [<ToDoList: Tims List>]>

In [5]: t
Out[5]: <ToDoList: Tims List>

In [6]: t.item_set.all()
Out[6]: <QuerySet []>

In [7]: t.item_set.create(text="go to the mall",complete=False)
Out[7]: <Item: go to the mall>

In [8]: t.item_set.all()
Out[8]: <QuerySet [<Item: go to the mall>]>

In [9]: exit()


In [2]: from main.models import Item, ToDoList

In [3]: t=ToDoList.objects

In [4]: t.all()
Out[4]: <QuerySet [<ToDoList: Tims List>]>

In [5]: t.filter(name__startswith='Tim')
Out[5]: <QuerySet [<ToDoList: Tims List>]>

In [6]: t.filter(id=1)
Out[6]: <QuerySet [<ToDoList: Tims List>]>

In [7]: t.filter(id=2)
Out[7]: <QuerySet []>

In [8]: del_object=t.get(id=1)

In [9]: del_object.delete()
Out[9]: (2, {'main.Item': 1, 'main.ToDoList': 1})
'''


class ToDoList(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    


class Item(models.Model):
    todoList=models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete=models.BooleanField()
    
    def __str__(self):
        return self.text
    
    
    

    
    
    
    
    