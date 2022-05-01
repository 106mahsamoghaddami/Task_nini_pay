from django.db import models
from django.db.models import Q


class ProductManager(models.Manager):
    def inventory(self, item):
        return self.filter(Q(brand__brand_name=item, count__gte=10) | Q(subcategory__category__name=item, count__gte=10))
