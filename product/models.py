from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'


class SubCategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sub_categories'


class LowerCategory(models.Model):
    sub_category = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'lower_categories'


class Brand(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'brands'

class Product(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    coupon = models.ForeignKey('account.Coupon', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    delivery_fee = models.IntegerField(default=0)

    class Meta:
        db_table = 'products'

class Additional(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'additionals'

class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    url = models.URLField()

    class Meta:
        db_table = 'images'

class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)
    image = models.URLField(blank=True)
    content = models.TextField()
    agreement = models.BooleanField(default=0)

    class Meta:
        db_table = 'reviews'
