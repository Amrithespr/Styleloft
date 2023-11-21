from django.contrib import admin
from .models import FemaleShop1, FemaleShop2, FemaleShop3, FemaleShop4, MaleShop1, MaleShop2, MaleShop3, MaleShop4, \
    FemaleService, ReviewFemaleShop1

# Register your models here.


admin.site.register(FemaleShop1)
admin.site.register(FemaleShop2)
admin.site.register(FemaleShop3)
admin.site.register(FemaleShop4)

admin.site.register(MaleShop1)
admin.site.register(MaleShop2)
admin.site.register(MaleShop3)
admin.site.register(MaleShop4)

admin.site.register(ReviewFemaleShop1)

admin.site.register(FemaleService)