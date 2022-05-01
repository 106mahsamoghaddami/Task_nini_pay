from rest_framework import serializers
from product.models import Shampoo
from django.contrib.auth.models import User


class ShampooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shampoo
        fields = "__all__"


