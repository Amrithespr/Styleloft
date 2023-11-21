from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string

from shopowner.models import ShopOwner, PasswordResetRequest, Referal
from bookingapp.models import FemaleShop1, FemaleShop2,FemaleShop3, FemaleShop4,MaleShop1,MaleShop2,MaleShop3,MaleShop4
from styleapp.views import logout


# Create your views here.




# def owner_registration(request):
#     a2 = ShopOwner.objects.all()
#     if request.method == "POST":
#         username = request.POST.get('username', '')
#         shop_name = request.POST.get('shop_name', '')
#         password = request.POST.get('password', '')
#         email = request.POST.get('email', '')
#         referal = request.POST.get('referal', '')
#
#         if ShopOwner.objects.filter(username=username).exists():
#             messages.info(request,'username already taken')
#             return redirect('/shopowner')
#         elif ShopOwner.objects.filter(email=email).exists():
#             messages.info(request,'email already taken')
#             return redirect('/shopowner')
#         else:
#             Shopowner = ShopOwner(username=username, shop_name=shop_name, password=password, email=email, referal=referal)
#             Shopowner.save()
#             messages.info(request, "Registered successfully")
#             return redirect('/shopowner')
#     return render(request, "shopowner.html", {'Shopowner': a2})


# def owner_login(request):
#     ab=ShopOwner.objects.all()
#     if request.method == 'POST':
#         shopname = request.POST['shopname']
#         password = request.POST['password']
#         print(shopname)
#         print(password)
#
#         if  ShopOwner.objects.filter(shop_name=shopname) and ShopOwner.objects.filter(password=password):
#             shopowner=ShopOwner.objects.get(shop_name=shopname)
#             path = shopowner.path
#             return redirect(path)
#
#         else:
#             # Invalid username/password
#             print("else")
#             messages.error(request, 'Invalid username/password')
#             return redirect('/shopowner')
#
#     return render(request, 'shopowner.html')



def owner_registration(request):
    a2 = ShopOwner.objects.all()
    if request.method == "POST":
        username = request.POST.get('username', '')
        shop_name = request.POST.get('shop_name', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        referal = request.POST.get('referal', '')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect('/shopowner')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            shop_owner = ShopOwner(username=username, shop_name=shop_name, email=email, referal=referal, user=user)
            shop_owner.save()
            messages.info(request, "Registered successfully")
            return redirect('/shopowner')
    return render(request, "shopowner.html", {'Shopowner': a2})



def owner_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            try:
                shop_owner = ShopOwner.objects.get(user=user)
                path = shop_owner.path  # Use the correct attribute name 'path'
                return redirect(path)
            except ShopOwner.DoesNotExist:
                messages.info(request, 'Shop owner details not found')
                return redirect('/shopowner#section_2')
        else:
            messages.info(request, 'Invalid username/password')
            return redirect('/shopowner')
    return render(request, 'shopowner.html')


def logout_shopowner(request):
    logout(request)
    return redirect('shopowner:owner_login')  # Redirect to your shopowner login page

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

def reset_owner_password(request):
    # Custom logic for the password reset view if needed
    return PasswordResetView.as_view()(request)

def reset_owner_password_done(request):
    return PasswordResetDoneView.as_view()(request)

def reset_owner_password_confirm(request, uidb64, token):
    return PasswordResetConfirmView.as_view()(request, uidb64=uidb64, token=token)

def reset_owner_password_complete(request):
    return PasswordResetCompleteView.as_view()(request)



# def forgotpassword(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         old = request.POST['oldpassword']
#         new = request.POST['newpassword']
#         confirm = request.POST['confirm']
#         if  ShopOwner.objects.filter(username=username) and ShopOwner.objects.filter(password=old):
#             if new==confirm:
#                 Shopowner = ShopOwner(username=username, password=new)
#                 Shopowner.save()
#                 messages.info(request, "Password changed successfully")
#                 return redirect('shopowner/')
#             else:
#                 messages.info(request, "Confirm your password")
#                 return redirect('forgotpassword/')
#         else:
#             messages.info(request, "you are not registered")
#             return redirect('forgotpassword/')
#     return render(request, 'forgotpassword.html')




# def request_reset_password(request):
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     security_answer = request.POST['security_answer']
    #     new_password = request.POST['new_password']
    #     try:
    #         shop_owner = ShopOwner.objects.get(email=email)
    #         security_question = shop_owner.security_qn
    #         if shop_owner.security_ans == security_answer:
    #             shop_owner.password = make_password(new_password)
    #             shop_owner.save()
    #             messages.success(request, 'Password changed successfully')
    #             return redirect('shopowner:reset_password')  # Update the redirect path
    #         else:
    #             messages.error(request, 'Invalid security answer')
    #     except ShopOwner.DoesNotExist:
    #         messages.error(request, 'Invalid email address')
    # else:
    #     # If it's a GET request, retrieve the security question
    #     email = request.GET.get('email')
    #     if email:
    #         try:
    #             shop_owner = ShopOwner.objects.get(email=email)
    #             security_question = shop_owner.security_qn
    #         except ShopOwner.DoesNotExist:
    #             messages.error(request, 'Invalid email address')
    #             return redirect('shopowner:reset_password')  # Update the redirect path
    #     else:
    #         messages.error(request, 'Invalid email address')
    #         return redirect('shopowner:reset_password')  # Update the redirect path
    #
    # context = {
    #     'email': email,
    #     'security_question': security_question
    # }
    # return render(request, 'reset_password.html', context)
    # return render(request, 'reset_password.html')





def Femaleshopowner1(request):
    a1 = FemaleShop1.objects.all()
    return render(request, 'female_shopowner1.html',  {'a': a1})

def Femaleshopowner2(request):
    b1 = FemaleShop2.objects.all()
    return render(request, 'female_shopowner2.html',  {'b': b1})

def Femaleshopowner3(request):
    c1 = FemaleShop3.objects.all()
    return render(request, 'female_shopowner3.html',  {'c': c1})

def Femaleshopowner4(request):
    d1 = FemaleShop4.objects.all()
    return render(request, 'female_shopowner4.html',  {'d': d1})



def Maleshopowner1(request):
    e1 = MaleShop1.objects.all()
    return render(request, 'male_shopowner1.html',  {'e': e1})

def Maleshopowner2(request):
    f1 = MaleShop2.objects.all()
    return render(request, 'male_shopowner2.html',  {'f': f1})

def Maleshopowner3(request):
    g1 = MaleShop3.objects.all()
    return render(request, 'male_shopowner3.html',  {'g': g1})

def Maleshopowner4(request):
    h1 = MaleShop4.objects.all()
    return render(request, 'male_shopowner4.html',  {'h': h1})


def Referals(request):
    referals = Referal.objects.all()
    return render(request, 'referal.html', {'referal': referals})





 # if request.method == 'POST':
    #     shopname = request.POST['shopname']
    #     password = request.POST['password']
    #
    #     user = authenticate(request, shop_name=shopname, password=password)
    #     print(user)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('Shopowner.path')
    #     else:
    #         messages.info(request,'Invalid username/password')
    #         return redirect('/shopowner')
    # return render(request,'shopowner.html')


# Authenticate the user
# user = authenticate(request, username=shopname, password=password)
# print(user)
# if user is not None:
#     # Log in the user
#     print("if")
#     login(request, user)