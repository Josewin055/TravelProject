from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Quotes
# Create your views here
def demo(request):
    obj=Place.objects.all()
    obj1=Quotes.objects.all()
    return render(request,"index.html",{'result':obj,'details':obj1})

# def addition(request):
#     X=int(request.GET['num1'])
#     Y=int(request.GET['num2'])
#     res=X+Y
#     return render(request,"result.html",{'result':res})