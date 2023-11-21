from . import views
from django.urls import path, include

app_name = 'bookingapp'

urlpatterns = [

    path('', views.addFemaleShop1, name='add'),
    path('addFemaleshop2/', views.addFemaleShop2, name='addFemaleshop2'),
    path('addFemaleshop3/', views.addFemaleShop3, name='addFemaleshop3'),
    path('addFemaleshop4/', views.addFemaleShop4, name='addFemaleshop4'),

    path('reviewFemaleShop1/', views.reviewFemaleShop1, name='reviewFemaleShop1'),

    path('addMaleshop1/', views.addMaleShop1, name='addMaleshop1'),
    path('addMaleshop2/', views.addMaleShop2, name='addMaleshop2'),
    path('addMaleshop3/', views.addMaleShop3, name='addMaleshop3'),
    path('addMaleshop4/', views.addMaleShop4, name='addMaleshop4'),

    path('detail/', views.detail, name='detail'),

    path('delete/<int:id>/', views.delete, name='delete'),
    path('payment/', views.payment, name='payment'),
]
