from django.db import models

# Create your models here.



class SaloonFemale(models.Model):
    image = models.ImageField(upload_to='SaloonFemale', blank=True)
    path = models.CharField(max_length=250)
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'saloonfemale'
        verbose_name_plural = 'saloonsfemale'

    def __str__(self):
        return '{}'.format(self.image)



class SaloonMale(models.Model):
    image = models.ImageField(upload_to='SaloonMale', blank=True)
    path = models.CharField(max_length=250)
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'saloonmale'
        verbose_name_plural = 'saloonsmale'

    def __str__(self):
        return '{}'.format(self.image)



class FemaleServices(models.Model):
    service = models.CharField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offerprice = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'femaleservice'
        verbose_name_plural = 'femaleservices'

    def __str__(self):
        return '{}'.format(self.service)

class MaleServices(models.Model):
    service = models.CharField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offerprice = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        verbose_name = 'maleservice'
        verbose_name_plural = 'maleservices'

    def __str__(self):
        return '{}'.format(self.service)