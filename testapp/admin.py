from django.contrib import admin
from testapp.models import Products
# Register your models here.
class Productadmin(admin.ModelAdmin):
    list_display=['Productname','CostPrice','Country','ORD_DATE','ORD_DESCRIPTION','Discount','Sellingprice']
admin.site.register(Products,Productadmin)
