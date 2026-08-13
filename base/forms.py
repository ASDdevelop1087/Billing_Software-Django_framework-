from django.forms import ModelForm
from .models import Product,Categorie


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        

class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'
