from django.urls import path
from . import views
urlpatterns = [
    path('',views.ShampooMoreThanTen.as_view(),name='filter_products' ),
    path('coffee/',views.CoffeeMoreThanTen.as_view(),name='coffee_products' ),




]