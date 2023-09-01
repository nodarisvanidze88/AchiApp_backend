from email.encoders import encode_noop
from json import JSONDecodeError
import os
import csv
from io import TextIOWrapper
from typing import TextIO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductList
from django.db import IntegrityError
from django.http import JsonResponse

@api_view(['POST'])
def getCSVFile(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES.get('csv_file')
        file = csv.DictReader(TextIOWrapper(csv_file, encoding='utf-8-sig'))
        header_items = list(file.fieldnames)
        imagesList = os.listdir('media/images')
        print(imagesList)
        for row in file:
            id = row[header_items[1]]
            imageName = f"{id}.jpg"
            try:
                instance = ProductList.objects.get(id=id)
                instance.code = row[header_items[0]]
                instance.item_name = row[header_items[2]]
                instance.category_name = row[header_items[3]]
                instance.dimention = row[header_items[4]]
                instance.warehouse = row[header_items[5]]
                instance.qty_in_wh = row[header_items[6]]
                instance.price = row[header_items[7]]
                if imageName in imagesList:
                    instance.image_urel = f'images/{imageName}'
                else:
                    instance.image_urel = ''
                instance.save()
            except ProductList.DoesNotExist:
                instance = ProductList(
                    code = row[header_items[0]],
                    id = row[header_items[1]],
                    item_name = row[header_items[2]],
                    category_name = row[header_items[3]],
                    dimention = row[header_items[4]],
                    warehouse = row[header_items[5]],
                    qty_in_wh = row[header_items[6]],
                    price = row[header_items[7]],
                    image_urel = f'images/{imageName}',
                )
                instance.save()
        resValue = JsonResponse({"hello":'uploaded'})
        return resValue
    else:
        resValue2 = JsonResponse({'goodby':'fuckyou'})
        return resValue2

@api_view(['GET'])
def getItemsList(request):
    if request.method=='GET':
        items = ProductList.objects.all()
        data = [{
            'code': i.code,
            'id': i.id,
            'item_name': i.item_name,
            'category_name': i.category_name,
            'dimention': i.dimention,
            'warehouse': i.warehouse,
            'qty_in_wh': i.qty_in_wh,
            'price': i.price,
            'image_urel': i.image_urel.url if i.image_urel else ''} for i in items]
        return JsonResponse(data, safe=False)