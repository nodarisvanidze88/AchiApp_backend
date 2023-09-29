from django.urls import path,include
from .views import getCSVFile, getItemsList, getWithoutImage, getUsers, addCollectedData, CustomersList
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register(r'customers',CustomersList, basename="customerList" )


urlpatterns = [
    path('test', getCSVFile, name="csvFile"),
    path('allItems', getItemsList, name='itemlist'),
    path('withoutimages', getWithoutImage, name='withoutImages'),
    path('getusers', getUsers, name="getusers"),
    path('add_collection_data', addCollectedData, name="collectedData"),
]
urlpatterns += route.urls
