from django.contrib import admin
from .models import TextRequest,Test
from .serializer import TextRequestSerializer

admin.site.register(TextRequest)
admin.site.register(Test)
