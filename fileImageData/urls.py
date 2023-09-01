from django.urls import path
from .views import getCSVFile, getItemsList
from django.views import View


urlpatterns = [
    path('test', getCSVFile, name="csvFile"),
    path('allItems', getItemsList, name='itemlist')
]