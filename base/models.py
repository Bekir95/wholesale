from typing import Any
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Product(models.Model):
    asin = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    price = models.FloatField(max_length=10)
    deal = models.FloatField(null=True, blank=True, max_length=10)

    def __str__(self):
        return self.asin


class ProductDetails(models.Model):
    asin = models.CharField(max_length=10,null=True, blank=True)
    salesRank = models.IntegerField(null=True, blank=True)
    salePrice = models.FloatField()
    amazon_fee = models.FloatField(null=True, blank=True)
    pick_and_pack_fee = models.FloatField(null=True, blank=True)
    
    profit = models.FloatField()
    profit_Percentage = models.FloatField()
    sales_Count = models.IntegerField(null=True, blank=True,)
    sellers_Count = models.IntegerField(null=True, blank=True,)
    weigt = models.FloatField(max_length=10)
    dimensions = models.CharField(max_length=30)
    variation_count = models.IntegerField()
    amzPrices = models.TextField(null=True, blank=True)
    fbaPrices = models.TextField(null=True, blank=True)
    fbmPrices = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.asin

    """
    def __init__(self, salesRank, salePrice, profit, profit_Percentage, sales_Count, weigt, dimensions, variation_count):
        self.salesRank = salesRank
        self.salePrice = salePrice
        self.profit = profit
        self. profit_Percentage = profit_Percentage
        self.sales_Count = sales_Count
        self.weigt = weigt
        self.dimensions = dimensions
        self.variation_count = variation_count
    #Keepa Grafiği
"""

class ProductDetailsUS(ProductDetails):
  pass

class ProductDetailsCA(ProductDetails):
  pass

class ProductDetailsUK(ProductDetails):
  pass
