from urllib.parse import quote

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from shopowner.models import Referal
from .models import SaloonFemale, SaloonMale, FemaleServices, MaleServices

# Create your views here.

# def index(request):
#     # Customize the message to join your app
#     message = "Join my awesome app!  " \
#               "Earn more customers and surprising rewards. " \
#               "Use the referal code as shared person's username. " \
#               "Follow the link to join." \
#               "http://127.0.0.1:8000/"
#
#
#
#         # URL encode the message
#     encoded_message = quote(message)
#
#     # Sharing URLs for different platforms
#     whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_message}"
#     instagram_url = f"https://www.instagram.com/?message={encoded_message}"
#     telegram_url = f"https://telegram.me/share/url?url={request.build_absolute_uri()}&text={encoded_message}"
#
#     return render(request, 'index.html', {
#         'whatsapp_url': whatsapp_url,
#         'instagram_url': instagram_url,
#         'telegram_url': telegram_url,
#     })
#



from urllib.parse import quote


# def index(request):
#
#     # Customize the message to join your app
#     message = "Join my awesome app!  " \
#               "Earn more customers and surprising rewards. " \
#               "Use the referral code as the shared person's username. " \
#               "Follow the link to join:"
#
#     # Get the absolute URL for the current view
#     url = request.build_absolute_uri(reverse('styleapp:index'))
#
#     # Append the link to the message
#     full_message = f"{message}\n\n{url}"
#
#     # URL encode the message
#     encoded_message = quote(full_message)
#
#     # Sharing URLs for different platforms
#     whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_message}"
#     instagram_url = f"https://www.instagram.com/?message={encoded_message}"
#     telegram_url = f"https://telegram.me/share/url?url={url}&text={encoded_message}"
#     # referals = Referal.objects.filter(name=request.user)
#
#
#     return render(request, 'index.html', {
#         'whatsapp_url': whatsapp_url,
#         'instagram_url': instagram_url,
#         'telegram_url': telegram_url,
#         # 'x':referals,
#     })

def index(request):
    # Customize the message to join your app
    message = "Join my awesome app!  " \
              "Earn more customers and surprising rewards. " \
              "Use the referral code as the shared person's username. " \
              "Follow the link to join:"

    # Get the absolute URL for the current view
    url = request.build_absolute_uri(reverse('styleapp:shopowner'))

    # Append the link to the message
    full_message = f"{message}\n\n{url}"

    # URL encode the message
    encoded_message = quote(full_message)

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get the currently logged-in user
        current_user = request.user

        # Filter Referal objects based on the currently logged-in user
        referals = Referal.objects.filter(name=current_user)
    else:
        # If the user is not logged in, set referals to an empty list
        referals = []

    whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_message}"
    instagram_url = f"https://www.instagram.com/?message={encoded_message}"
    telegram_url = f"https://telegram.me/share/url?url={url}&text={encoded_message}"

    return render(request, 'index.html', {
        'whatsapp_url': whatsapp_url,
        'instagram_url': instagram_url,
        'telegram_url': telegram_url,
        'x': referals,  # Pass the filtered referals to the template
    })



def shop_listing_female(request):
    saloon_female = SaloonFemale.objects.all()
    context = {
        'saloon_list': saloon_female
    }
    return render(request, "shop-listing-female.html", context)

def shop_listing_male(request):
    saloon_male = SaloonMale.objects.all()
    context = {
        'saloon_list': saloon_male
    }
    return render(request, "shop-listing-male.html", context)




      # credentiails

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid username/password')
            return redirect('/login#section_6')
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username already taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email already taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            print('User created')
            messages.info(request,"Registered successfully")
            return redirect('/#section_6')
    return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def shopowner(request):
    return render(request, "shopowner.html")

def female_services(request):
    m1=FemaleServices.objects.all()
    return render(request, "female services.html", {'m': m1})

def male_services(request):
    n1=MaleServices.objects.all()
    return render(request, "male services.html", {'n': n1})



def share_app(request):
    # Customize the message to join your app
    message = "Join my awesome app!"

    # URL encode the message
    encoded_message = quote(message)

    # Sharing URLs for different platforms
    whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_message}"
    instagram_url = f"https://www.instagram.com/?message={encoded_message}"
    telegram_url = f"https://telegram.me/share/url?url={request.build_absolute_uri()}&text={encoded_message}"

    return render(request, 'index.html', {
        'whatsapp_url': whatsapp_url,
        'instagram_url': instagram_url,
        'telegram_url': telegram_url,
    })


