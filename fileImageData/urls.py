from django.urls import path
from .views import getCSVFile, getItemsList, getWithoutImage, getUsers



urlpatterns = [
    path('test', getCSVFile, name="csvFile"),
    path('allItems', getItemsList, name='itemlist'),
    path('withoutimages', getWithoutImage, name='withoutImages'),
    path('getusers', getUsers, name="getusers"),
]
