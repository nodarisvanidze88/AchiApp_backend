from django.contrib import admin
from .models import ProductList, Users
# Register your models here.
admin.site.register({ProductList,Users})
