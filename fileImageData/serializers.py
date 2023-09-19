from rest_framework import serializers
from .models import CollectedProduct

class CollectedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedProduct
        fields= ['user','product_ID','quantity', 'date']