from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ProductForm, CategorieForm

from base.models import Product, Categorie

# Create your views here.


def home(request):
    return render(request, "base/home.html")


def catalogue(request):
    # Fetching data from models
    all_products = Product.objects.all()
    all_categories = Categorie.objects.all()

    # context dictionary
    context = {
        'products': all_products,       # Key used in template: {{ products }}
        # Key used in template: {{ categories }}
        'categories': all_categories,
        'num': 0,
    }
    return render(request, "base/catalogue.html", context)


def main(request):
    return render(request, "main.html")


def create_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "base/product_form.html", context)


def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {'form': form}
    return render(request, "base/product_form.html", context)


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'obj': product}
    if request.method == "POST":
        product.delete()
        return redirect('catalogue')
    return render(request, "base/confirmation.html", context)


def create_categorie(request):
    form = CategorieForm()
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "base/category_form.html", context)


def update_categorie(request, pk):
    categorie = Categorie.objects.get(id=pk)
    form = CategorieForm(instance=categorie)
    if request.method == "POST":
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {'form': form}
    return render(request, "base/category_form.html", context)


def delete_categorie(request, pk):
    categorie = Categorie.objects.get(id=pk)
    context = {'obj': categorie}
    if request.method == "POST":
        categorie.delete()
        return redirect('catalogue')
    return render(request, "base/confirmation.html", context)
