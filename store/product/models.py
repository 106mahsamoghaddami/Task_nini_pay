from django.db import models
from django.utils import timezone
from .manager import ProductManager

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    established_year = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    price = models.IntegerField()
    barcode = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField()
    production_year = models.DateField( blank=True, null=True)
    expiration = models.DateField(blank=True, null=True)
    made_in = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    class Meta:
        abstract = True  # i don't want to create a table for product , I just want to use it as a parent class

    def __str__(self):
        return self.name


class TShirt(Product):
    type_choice = [
        ('Cotton', 'نخ پنبه'),
        ('Plastic', 'پلاستیک'),
        ('Tetron', 'تترون'),
        ('Lee', 'لی'),
        ('Raven', 'ریون'),
        ('Velvet', 'مخمل'),

    ]
    size_choice = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'large'),
        ('Xl', 'XLarge'),
        ('2xL', '2XLarge'),
        ('3xL', '3XLarge'),
        ('4xL', '4XLarge'),
        ('5xL', '5XLarge'),

    ]
    cloth_type = models.CharField(max_length=10, choices=type_choice, null=True)
    size = models.CharField(max_length=3, choices=size_choice, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    objects = ProductManager()
    def __str__(self):
        return f"TShirt:{self.name} with  size : {self.size}  "


class Shampoo(Product):
    choice_kind = [
        ('dry', 'dry hair'),
        ('oily', 'oily hair'),
        ('normal', 'normal hair'),
        ('childish', 'childish'),
        ('conditioner', 'conditioner'),
    ]
    shampoo_type = models.CharField(max_length=20, choices=choice_kind, null=True)
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    objects = ProductManager()
    def __str__(self):
        return f"shampoo {self.name}  {self.brand} for {self.shampoo_type} hair "


class Coffee(Product):
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    package_weight = models.IntegerField()

    objects = ProductManager()

    def __str__(self):
        return f"coffee {self.name} package_weight:{self.package_weight} gr "
