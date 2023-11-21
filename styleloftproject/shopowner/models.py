from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ShopOwner(models.Model):
    username = models.CharField(max_length=250)
    shop_name = models.CharField(max_length=250)
    password = models.SlugField(max_length=250,blank=True)
    email = models.EmailField(max_length=250)
    path = models.CharField(max_length=250)
    referal = models.CharField(max_length=250,blank=True)
    user = models.CharField(max_length=250,blank=True)



    class Meta:
        verbose_name = 'shopowner'
        verbose_name_plural = 'shopowners'

    def __str__(self):
        return '{}'.format(self.shop_name)



class Referal(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    No_of_offers = models.CharField(max_length=250, blank=True)


    class Meta:
        verbose_name = 'referal'
        verbose_name_plural = 'referals'

    def __str__(self):
        return '{}'.format(self.name)



class PasswordResetRequest(models.Model):
    shop_owner = models.ForeignKey(ShopOwner, on_delete=models.CASCADE)
    token = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)



