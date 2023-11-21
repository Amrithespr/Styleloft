from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'styleapp'

urlpatterns = [

    path('', views.index, name='index'),

    path('shop_listing_female/', views.shop_listing_female, name='shop_listing_female'),
    path('shop_listing_male/', views.shop_listing_male, name='shop_listing_male'),

    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('shopowner/', views.shopowner, name='shopowner'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),




    path('male_services/', views.male_services, name='male_services'),
    path('female_services/', views.female_services, name='female_services'),

]
