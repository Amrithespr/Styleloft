from django.contrib import messages
from django.http import request
from django.shortcuts import render, redirect


from .models import FemaleShop1, FemaleShop2, FemaleShop3, FemaleShop4, MaleShop1, MaleShop2, MaleShop3, MaleShop4, \
    ReviewFemaleShop1


def addFemaleShop1(request):
    a1 = FemaleShop1.objects.all()
    c1 = ReviewFemaleShop1.objects.all()
    if request.method == "POST":
        name = request.POST.get('username', '')
        service = request.POST.get('service', '')
        date = request.POST.get('date' '')
        time = request.POST.get('time' '')
        phone = request.POST.get('phone' '')
        if not FemaleShop1.objects.filter(date=date , time=time).exists():
            a = FemaleShop1(name=name, service=service, date=date, time=time, phone=phone)
            a.save()
            # return redirect('/bookingapp/payment')
            return redirect('/bookingapp#section_4')
        else:
            messages.info(request, 'This timeslot is already Booked')
            return redirect('/bookingapp#section_4')
    return render(request, "female_shop1.html", {'a': a1, 'c': c1})

def delete(request, id):
    if request.method == 'POST':
        task = FemaleShop1.objects.get(id=id)
        task.delete()
        return redirect('/bookingapp#section_4')
    return render(request, "delete.html")

def detail(request):
    a1 = FemaleShop1.objects.all()
    if request.user.is_authenticated:
        # Get the currently logged-in user
        current_user = request.user

        # Filter Referal objects based on the currently logged-in user
        referals = FemaleShop1.objects.filter(name=current_user)
    else:
        # If the user is not logged in, set referals to an empty list
        referals = []
    return render(request, "female_shop1_delete.html", {'a': referals,'a1':a1})


def reviewFemaleShop1(request):

    if request.method == "POST":
        name =  request.POST.get('username', '')
        review = request.POST.get('review', '')
        review1 = ReviewFemaleShop1(review=review,name=name)
        review1.save()
        return redirect('/bookingapp#section_4')
    return render(request, "female_shop1.html")


def addFemaleShop2(request):
    b1 = FemaleShop2.objects.all()
    if request.method == "POST":
        name = request.POST.get('username', '')
        service = request.POST.get('service', '')
        date = request.POST.get('date' '')
        time = request.POST.get('time' '')
        phone = request.POST.get('phone' '')
        if not FemaleShop2.objects.filter(date=date , time=time).exists():
            b = FemaleShop2(name=name, service=service, date=date, time=time, phone=phone)
            b.save()
            return redirect('/bookingapp/addFemaleshop2#section_2')
        else:
            messages.info(request, 'This timeslot is already Booked')
            return redirect('/bookingapp/addFemaleshop2#section_4')
    return render(request, "female_shop2.html", {'b': b1})

def addFemaleShop3(request):
    c1 = FemaleShop3.objects.all()
    if request.method == "POST":
        name = request.POST.get('username', '')
        service = request.POST.get('service', '')
        date = request.POST.get('date' '')
        time = request.POST.get('time' '')
        phone = request.POST.get('phone' '')
        if not FemaleShop3.objects.filter(date=date , time=time).exists():
            c = FemaleShop3(name=name, service=service, date=date, time=time, phone=phone)
            c.save()
            return redirect('/bookingapp/payment')
        else:
            messages.info(request, 'This timeslot is already Booked')
            return redirect('/bookingapp/addFemaleshop3#section_4')
    return render(request, "female_shop3.html", {'c': c1})

def addFemaleShop4(request):
    d1 = FemaleShop4.objects.all()
    if request.method == "POST":
        name = request.POST.get('username', '')
        service = request.POST.get('service', '')
        date = request.POST.get('date' '')
        time = request.POST.get('time' '')
        phone = request.POST.get('phone' '')
        if not FemaleShop4.objects.filter(date=date , time=time).exists():
            d = FemaleShop4(name=name, service=service, date=date, time=time, phone=phone)
            d.save()
            return redirect('/bookingapp/addFemaleshop4#section_2')
        else:
            messages.info(request, 'This timeslot is already Booked')
            return redirect('/bookingapp/addFemaleshop4#section_4')
    return render(request, "female_shop4.html", {'d': d1})

def addMaleShop1(request):
    e1 = MaleShop1.objects.all()
    if request.method == "POST":
        name = request.POST.get('username', '')
        service = request.POST.get('service', '')
        date = request.POST.get('date' '')
        time = request.POST.get('time' '')
        phone = request.POST.get('phone' '')
        if not MaleShop1.objects.filter(date=date , time=time).exists():
            e = MaleShop1(name=name, service=service, date=date, time=time, phone=phone)
            e.save()
            return redirect('/bookingapp/addMaleShop1#section_2')
        else:
            messages.info(request, 'This timeslot is already Booked')
            return redirect('/bookingapp/addMaleShop1#section_4')
    return render(request, "Male_shop1.html", {'e': e1})

def addMaleShop2(request):
    f1 = MaleShop2.objects.all()
    if request.method == "POST":
        name = request.POST.get('username', '')
        service = request.POST.get('service', '')
        date = request.POST.get('date' '')
        time = request.POST.get('time' '')
        phone = request.POST.get('phone' '')
        if not MaleShop2.objects.filter(date=date , time=time).exists():
            f = MaleShop2(name=name, service=service, date=date, time=time, phone=phone)
            f.save()
            return redirect('/bookingapp/addMaleShop2#section_2')
        else:
            messages.info(request, 'This timeslot is already Booked')
            return redirect('/bookingapp/addMaleShop2#section_4')
    return render(request, "Male_shop2.html", {'f': f1})

def addMaleShop3(request):
    g1 = MaleShop3.objects.all()
    if request.method == "POST":
        name = request.POST.get('username', '')
        service = request.POST.get('service', '')
        date = request.POST.get('date' '')
        time = request.POST.get('time' '')
        phone = request.POST.get('phone' '')
        if not MaleShop3.objects.filter(date=date , time=time).exists():
            g = MaleShop3(name=name, service=service, date=date, time=time, phone=phone)
            g.save()
            return redirect('/bookingapp/addMaleshop3#section_2')
        else:
            messages.info(request, 'This timeslot is already Booked')
            return redirect('/bookingapp/addMaleshop3#section_4')
    return render(request, "Male_shop3.html", {'b': g1})

def addMaleShop4(request):
    h1 = MaleShop4.objects.all()
    if request.method == "POST":
        name = request.POST.get('username', '')
        service = request.POST.get('service', '')
        date = request.POST.get('date' '')
        time = request.POST.get('time' '')
        phone = request.POST.get('phone' '')
        if not MaleShop4.objects.filter(date=date , time=time).exists():
            h = MaleShop4(name=name, service=service, date=date, time=time, phone=phone)
            h.save()
            return redirect('/bookingapp/addMaleshop4#section_2')
        else:
            messages.info(request, 'This timeslot is already Booked')
            return redirect('/bookingapp/addMaleshop4#section_4')
    return render(request, "Male_shop4.html", {'h': h1})

def payment(request):
    return render(request, "payment.html")