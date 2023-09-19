from django.urls import path
from .views import getCSVFile, getItemsList, getWithoutImage, getUsers, addCollectedData



urlpatterns = [
    path('test', getCSVFile, name="csvFile"),
    path('allItems', getItemsList, name='itemlist'),
    path('withoutimages', getWithoutImage, name='withoutImages'),
    path('getusers', getUsers, name="getusers"),
    path('add_collection_data', addCollectedData, name="collectedData"),
]
