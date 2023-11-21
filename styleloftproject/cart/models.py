from django.contrib.auth.models import User
from django.db import models
from shop.models import Product


# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)


    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)

class OrderStatus(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=250, blank=True)


    class Meta:
        verbose_name = 'orderstatus'
        verbose_name_plural = 'orderstatus'

    def __str__(self):
        return '{}'.format(self.name)


class Delivary(models.Model):

    address_line_1 = models.CharField(max_length=250, blank=True)
    address_line_2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    postal_code = models.CharField(max_length=250, blank=True)
    mobile_number = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)
    name = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name = 'delivary'
        verbose_name_plural = 'delivary'

    def __str__(self):
        return '{}'.format(self.name)






