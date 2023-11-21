import razorpay
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from shop.models import Product
from .models import Cart, CartItem, OrderStatus, Delivary


# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save(),

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()
    return redirect('cart:cart_detail')


@login_required
def cart_detail(request, total=0, counter=0, cart_items=None, status=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    # Filter OrderStatus objects based on the user associated with the request
    user_status = OrderStatus.objects.filter(name=request.user)
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter, status=user_status))


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')


def full_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')


@csrf_exempt
def payment(request):
    # Razorpay credentials
    razorpay_key_id = "rzp_test_zddK1OzkWyN71o"
    razorpay_key_secret = "Q2RDsJ83DWNht8jtFtLK2EuB"

    client = razorpay.Client(auth=(razorpay_key_id, razorpay_key_secret))

    if request.method == 'POST':
        # Process the payment response
        response = request.POST
        order_id = response['razorpay_order_id']
        payment_id = response['razorpay_payment_id']
        signature = response['razorpay_signature']

        try:
            client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })
            # Payment successful, update the payment status in your system
            # return HttpResponse("Payment Successful")
            return redirect('/cart/checkout')
        except Exception as e:
            # Payment verification failed, handle the failure case
            return HttpResponse("Payment Verification Failed")
    else:
        # Get the total amount from the cart
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        total_amount = sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)

        # Generate unique order ID and other required parameters
        order_amount = int(total_amount * 100)  # Amount should be in paise (e.g., Rs 500 should be 50000)
        order_currency = "INR"
        order_receipt = "<generate_unique_order_receipt>"

        # Create an order in Razorpay
        order = client.order.create({
            'amount': order_amount,
            'currency': order_currency,
            'receipt': order_receipt,
            'payment_capture': '1'  # Auto-capture payment after successful redirect
        })

        # Create a context with necessary parameters
        context = {
            'order_id': order['id'],
            'order_amount': order_amount,
            'order_currency': order['currency'],
            'order_receipt': order['receipt'],
            'razorpay_key_id': razorpay_key_id
        }

        return render(request, "payment.html", context)

@login_required
def checkout(request):
    if request.method == "POST":
        address_line_1 = request.POST.get('address_line_1', '')
        address_line_2 = request.POST.get('address_line_2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        postal_code = request.POST.get('postal_code', '')
        mobile_number = request.POST.get('mobile_number', '')
        name = request.POST.get('name', '')
        email = request.POST.get('name', '')

        delivary = Delivary(address_line_1=address_line_1, address_line_2=address_line_2, city=city, state=state, postal_code=postal_code,mobile_number=mobile_number,name=name,email=email)
        delivary.save()
        return redirect('/shop')
    return render(request, "checkout.html")
