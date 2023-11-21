from .models import FemaleShop1, FemaleShop2, FemaleShop3, FemaleShop4, MaleShop1, MaleShop2, MaleShop3, MaleShop4, \
    ReviewFemaleShop1
from django import forms

class FemaleShop1Form(forms.ModelForm):
    class Meta:
        model=FemaleShop1
        fields=['name', 'service', 'date', 'time', 'phone']

class FemaleShop2Form(forms.ModelForm):
    class Meta:
        model=FemaleShop2
        fields=['name', 'service', 'date', 'time', 'phone']

class FemaleShop3Form(forms.ModelForm):
    class Meta:
        model=FemaleShop3
        fields=['name', 'service', 'date', 'time', 'phone']

class FemaleShop4Form(forms.ModelForm):
    class Meta:
        model=FemaleShop4
        fields=['name', 'service', 'date', 'time', 'phone']

class MaleShop1Form(forms.ModelForm):
    class Meta:
        model=MaleShop1
        fields=['name', 'service', 'date', 'time', 'phone']

class MaleShop2Form(forms.ModelForm):
    class Meta:
        model=MaleShop2
        fields=['name', 'service', 'date', 'time', 'phone']

class MaleShop3Form(forms.ModelForm):
    class Meta:
        model=MaleShop3
        fields=['name', 'service', 'date', 'time', 'phone']

class MaleShop4Form(forms.ModelForm):
    class Meta:
        model=MaleShop4
        fields=['name', 'service', 'date', 'time', 'phone']


class ReviewFemaleShop1Form(forms.ModelForm):
    class Meta:
        model=ReviewFemaleShop1
        fields=['name', 'review']