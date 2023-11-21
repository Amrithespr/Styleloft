from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views



app_name = 'shopowner'

urlpatterns = [

    path('owner_registration/', views.owner_registration, name='owner_registration'),
    path('owner_login/', views.owner_login, name='owner_login'),

    path('logout/', views.logout_shopowner, name='logout_shopowner'),

    path('reset_owner_password/', auth_views.PasswordResetView.as_view(), name='reset_owner_password'),
    path('reset_owner_password/done/', auth_views.PasswordResetDoneView.as_view(), name='reset_owner_password_done'),
    path('reset_owner_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='reset_owner_password_confirm'),
    path('reset_owner_password/complete/', auth_views.PasswordResetCompleteView.as_view(),name='reset_owner_password_complete'),


    path('referal/', views.Referals, name='referal'),

    path('Femaleshopowner1/', views.Femaleshopowner1, name='Femaleshopowner1'),
    path('Femaleshopowner2/', views.Femaleshopowner2, name='Femaleshopowner2'),
    path('Femaleshopowner3/', views.Femaleshopowner3, name='Femaleshopowner3'),
    path('Femaleshopowner4/', views.Femaleshopowner4, name='Femaleshopowner4'),

    path('Maleshopowner1/', views.Maleshopowner1, name='Maleshopowner1'),
    path('Maleshopowner2/', views.Maleshopowner2, name='Maleshopowner2'),
    path('Maleshopowner3/', views.Maleshopowner3, name='Maleshopowner3'),
    path('Maleshopowner4/', views.Maleshopowner4, name='Maleshopowner4'),

]
