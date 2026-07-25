from django.shortcuts import render
from django.http import HttpResponse

from base.models import Product,Categorie

# Create your views here.
def home(request):
    return render(request,"base/home.html")

def catalogue(request):
    #Fetching data from models
    all_products = Product.objects.all()
    all_categories = Categorie.objects.all()

    #context dictionary
    context = {
        'products': all_products,       # Key used in template: {{ products }}
        'categories': all_categories,   # Key used in template: {{ categories }}
    }
    return render(request,"base/catalogue.html",context)

def index(request):
    return render(request,"index.html")

def navbar(request):
    return render(request,"navbar.html")
