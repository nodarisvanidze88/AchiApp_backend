from django.db import models

# Create your models here.
class ProductList(models.Model):
    code = models.CharField(max_length=50)
    id = models.CharField(primary_key=True,max_length=50)
    item_name = models.CharField(max_length=200)
    category_name = models.CharField(max_length=50)
    dimention = models.CharField(max_length=50)
    warehouse = models.CharField(max_length=50) # code of warehouse
    qty_in_wh = models.FloatField() # quantity in warehouse
    price = models.FloatField()
    image_urel = models.URLField()

    def __str__(self):
        return self.item_name


