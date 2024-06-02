from django.contrib import admin
from .models import ProductType,Product,Sale,News,Vacancy,Questions,Rewiews,Promocode


admin.site.register(Promocode)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(News)
admin.site.register(Vacancy)
admin.site.register(Questions)
admin.site.register(Rewiews)

