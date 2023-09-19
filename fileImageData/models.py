
from django.db import models

# Create your models here.
class ProductList(models.Model):
    code = models.CharField(max_length=50)
    id = models.CharField(primary_key=True, max_length=50, unique=True)
    item_name = models.CharField(max_length=200)
    category_name = models.CharField(max_length=50)
    dimention = models.CharField(max_length=50)
    warehouse = models.CharField(max_length=50) # code of warehouse
    qty_in_wh = models.FloatField() # quantity in warehouse
    price = models.FloatField()
    image_urel = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.item_name

class Users(models.Model):
  user = models.CharField(max_length = 50, unique=True)

  def __str__(self):
        return self.user
  
class Customers(models.Model):
    identification = models.CharField(max_length=11, unique=True)
    customer_name = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=200)

    def __str__(self):
        return f'({self.identification}) - {self.customer_name}'

    


class CollectedProduct(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='supervizer')
    product_ID = models.ForeignKey(ProductList, on_delete=models.CASCADE, related_name='selectedItem')
    quantity = models.IntegerField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.date} {self.user} {self.product_ID} {self.quantity}"



