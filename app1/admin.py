from django.contrib import admin
from .models import MyOffice, MyModel
# Register your models here.

admin.site.register(MyModel)
admin.site.register(MyOffice)
