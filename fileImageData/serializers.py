from rest_framework import serializers
from .models import CollectedProduct
from .models import Customers

class CollectedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedProduct
        fields= ['user','product_ID','quantity', 'date']

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'