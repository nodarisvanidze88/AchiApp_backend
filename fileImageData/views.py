import os
import csv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductList
from django.db import IntegrityError

@api_view(['POST'])
def getCSVFile(request):
    if request.method == 'POST' and request.FILE.get('csv_file'):
        csv_file = request.FILE.get('csv_fiel')
        decoded_csv_file = csv_file.read().decode('utf-8')
        csv_data = csv.DictReader(decoded_csv_file.splitlines(), delimiter=",")

# Create your views here.
