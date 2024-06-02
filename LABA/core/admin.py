from django.contrib import admin
from .models import User, Admin, Zakazchik, Employee


admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Admin)
admin.site.register(Zakazchik)

