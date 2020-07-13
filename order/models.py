from django.db import models

class Cart(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('product.Product', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)

    class Meta:
        db_table = 'carts'

class Order(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('product.Product', on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey('cart', on_delete=models.SET_NULL, null=True)
    coupon = models.ForeignKey('account.Coupon', on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    address_detail = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    delivery_memo = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    point = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    class Meta:
        db_table = 'orders'

class Status(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'status'
