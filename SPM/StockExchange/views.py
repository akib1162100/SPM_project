from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
import json

# Create your views here.

with open(os.path.join(settings.BASE_DIR,'data.json')) as f:
    data_obj = json.load(f)

def home(request):
    context = {
        'data': data_obj
    }

    return render(request, 'StockExchange/data.html', context)