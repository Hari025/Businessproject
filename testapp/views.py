from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from testapp.models import Products
import csv
import datetime
def homeview(request):
    return render(request,'testapp/product.html')
# Create your views here.
def createpost(request):
        if request.method == 'POST':
            if request.POST.get('Productname') and request.POST.get('CostPrice') and request.POST.get('Country') and request.POST.get('ORD_DATE') and request.POST.get('ORD_DESCRIPTION')and request.POST.get('Discount')and request.POST.get('Sellingprice') :
                post=Products()
                post.Productname=request.POST.get('Productname')
                post.CostPrice= request.POST.get('CostPrice')
                post.Country= request.POST.get('Country')
                post.ORD_DATE= request.POST.get('ORD_DATE')
                post.ORD_DESCRIPTION= request.POST.get('ORD_DESCRIPTION')
                post.Discount= request.POST.get('Discount')
                post.Sellingprice= request.POST.get('Sellingprice')
                post.save()

                return render(request, 'testapp/product.html')
        else:
                return render(request,'testapp/list.html')
def some_view(request):
        prod=Products.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="PRODUCT_PRICELIST_{now}.csv"'.format(
        now = str(datetime.date.today())
        ).encode()
        writer = csv.writer(response)
        writer.writerow(['Productname','CostPrice','Country','ORD_DATE','ORD_DESCRIPTION','Discount','Sellingprice'])
        for prd in prod:
            writer.writerow([prd.Productname,prd.CostPrice,prd.Country,prd.ORD_DATE,prd.ORD_DESCRIPTION,prd.Discount,prd.Sellingprice])
        return response
