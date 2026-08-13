from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("catalogue/", views.catalogue, name="catalogue"),
    path("update-product/<str:pk>/", views.update_product, name="update-product"),
    path("create-product/", views.create_product, name="create-product"),
    path("delete-product/<str:pk>/", views.delete_product, name="delete-product"),
    path("update-category/<str:pk>/", views.update_categorie, name="update-category"),
    path("create-category/", views.create_categorie, name="create-category"),
    path("delete-category/<str:pk>/",views.delete_categorie, name="delete-category"),
]
