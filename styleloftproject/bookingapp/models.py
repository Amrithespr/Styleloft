from django.db import models


# Create your models here.

class FemaleShop1(models.Model):
    name     = models.CharField(max_length=250)
    service     = models.CharField(max_length=350)
    date     = models.DateField()
    time = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.service

class ReviewFemaleShop1(models.Model):
    name = models.CharField(max_length=250)
    review     = models.CharField(max_length=250)

    def __str__(self):
        return self.review

class FemaleShop2(models.Model):
    name     = models.CharField(max_length=250)
    service     = models.CharField(max_length=350)
    date     = models.DateField()
    time = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.service

class FemaleShop3(models.Model):
    name     = models.CharField(max_length=250)
    service     = models.CharField(max_length=350)
    date     = models.DateField()
    time = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.service

class FemaleShop4(models.Model):
    name     = models.CharField(max_length=250)
    service     = models.CharField(max_length=350)
    date     = models.DateField()
    time = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.service

class MaleShop1(models.Model):
    name     = models.CharField(max_length=250)
    service     = models.CharField(max_length=350)
    date     = models.DateField()
    time = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.service

class MaleShop2(models.Model):
    name     = models.CharField(max_length=250)
    service     = models.CharField(max_length=350)
    date     = models.DateField()
    time = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.service

class MaleShop3(models.Model):
    name     = models.CharField(max_length=250)
    service     = models.CharField(max_length=350)
    date     = models.DateField()
    time = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.service

class MaleShop4(models.Model):
    name     = models.CharField(max_length=250)
    service     = models.CharField(max_length=350)
    date     = models.DateField()
    time = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.service





class FemaleService(models.Model):

    service = models.CharField(max_length=350)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.service

