from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ProductForm, CategorieForm
from django.db.models import Q

from base.models import Product, Categorie

# Create your views here.


def home(request):
    return render(request, "base/home.html")


def catalogue(request):
    q = request.GET.get('q')
    
    if q:
        filtered_categories = Categorie.objects.filter(name__icontains=q)
        filtered_products = Product.objects.filter(
            Q(name__icontains=q) |
              Q(description__icontains=q))
    else:
        filtered_categories = Categorie.objects.all()
        filtered_products = Product.objects.all()
    uncategorized_products = Product.objects.filter(category__isnull=True)
    categories = Categorie.objects.all()
    context = {
        'products': filtered_products,
        'categories': categories,
        'filtered_categories': filtered_categories,
        'uncategorized_products': uncategorized_products,
        'q': q,
        'count': filtered_categories.count(),
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
