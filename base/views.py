from django.shortcuts import get_object_or_404, render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from base import models
# Create your views here.

rooms = [
    {'id':1, 'name':'Lets LEarn Python'},
    {'id':2, 'name':'Lets LEarn Java'},
    {'id':3, 'name':'Lets LEarn Django'},
]


def home(request):
    
    products_with_deals = Product.objects.filter(deal__gt=0)

    products_without_deals = Product.objects.filter(deal=0) | Product.objects.filter(deal=None)

    context = {'products_with_deals':products_with_deals,
               'products_without_deals':products_without_deals}
    return render(request, 'base/home.html', context)

def products(request):
    #products = Product.objects.all()
    p = Paginator(Product.objects.all(),8)
    page = request.GET.get('page')
    products = p.get_page(page)
    nums = "a" * products.paginator.num_pages
    context = {'products':products,
               'nums' : nums}
    return render(request, 'base/products.html', context)


def create_charts(instance):
    amzprices = [float(i) for i in instance.amzPrices.split(',')]
    fbaprices = [float(i) for i in instance.fbaPrices.split(',')]
    fbmprices = [float(i) for i in instance.fbmPrices.split(',')]
 
    
    prices = {'date' : np.arange(len(amzprices)),
              'amz' : amzprices,
              'fba' : fbaprices,
              'fbm' : fbmprices,
              'weight' : np.ones(len(amzprices))
              }
   
    pricesDF = pd.DataFrame(data=prices)
    

    figLine = px.line(pricesDF, x="date", y=['amz', 'fba', 'fbm'],
                  color_discrete_sequence=["orange", "red", "blue"])
   

    #fig = go.Figure([go.Scatter(x=np.arange(len(my_list)), y=my_list)])
    figLine.update_layout(autotypenumbers='convert types')
    
    
    

    chartLine = figLine.to_html()
   
    figPieAmz = px.pie(pricesDF, values='weight', names='amz',
                    title="Amazon Fiyat Dağılımı",
                    width=300, height=300)
    figPieAmz.update_layout(title_x=0.5)

    figPieFba = px.pie(pricesDF, values='weight', names='amz',
                    title="Fba Fiyat Dağılımı",
                    width=300, height=300)
    figPieFba.update_layout(title_x=0.5)

    chartPieAmz = figPieAmz.to_html()
    chartPieFba = figPieFba.to_html()

    charts = {'chartLine' : chartLine,
              'chartPieAmz' : chartPieAmz,
              'chartPieFba' : chartPieFba}
    
    return charts

def modal_view(request, pk):

    instance = get_object_or_404(models.Product, asin=pk)
    instanceUS = get_object_or_404(models.ProductDetailsUS, asin=pk)
    instanceCA = get_object_or_404(models.ProductDetailsCA, asin=pk)
    instanceUK = get_object_or_404(models.ProductDetailsUK, asin=pk)
    print(instanceUS)
    print(instanceCA)
    print(instanceUK)

    uk_charts = create_charts(instanceUK)
    us_charts = create_charts(instanceUS)
    ca_charts = create_charts(instanceCA)

    
    context={
        'product': instance,
        'productDetailsUS': instanceUS,
        'productDetailsCA': instanceCA,
        'productDetailsUK': instanceUK,
        'chartUSLine' : us_charts['chartLine'],
        'chartUSPieAmz' : us_charts['chartPieAmz'],
        'chartUSPieFba' : us_charts['chartPieFba'],
        'chartCALine' : ca_charts['chartLine'],
        'chartCAPieAmz' : ca_charts['chartPieAmz'],
        'chartCAPieFba' : ca_charts['chartPieFba'],
        'chartUKLine' : uk_charts['chartLine'],
        'chartUKPieAmz' : uk_charts['chartPieAmz'],
        'chartUKPieFba' : uk_charts['chartPieFba'],
    }
    return render(request, 'base/modal.html', context)



def adminImportUpdate(request):
    
    return render(request,'base/adminImportUpdate.html')