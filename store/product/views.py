from django.shortcuts import render
from django.views import View
from .models import TShirt, Shampoo, Coffee
from django.http import HttpResponseRedirect, HttpResponse


class ShampooMoreThanTen(View):
    def get(self, request):
        products = Shampoo.objects.inventory('golrang')

        return render(request, 'product/inventory.html', {'products': products})


class CoffeeMoreThanTen(View):
    def get(self, request):
        products = Coffee.objects.inventory('food')

        return render(request, 'product/inventory.html', {'products': products})
