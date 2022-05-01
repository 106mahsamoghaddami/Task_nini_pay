from django.shortcuts import render
from product.models import Shampoo
# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializer import ShampooSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


# -----------------------API---------------------------------------------------#

class Shampoolists(ListAPIView):
    queryset = Shampoo.objects.all()
    serializer_class = ShampooSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('brand',)

# def detail_product(request, brand_id):
#     product_obj = Shampoo.objects.filter(brand_id=brand_id)
#     ser_data = ShampooSerializer(product_obj)
#     return Response(ser_data.data)
