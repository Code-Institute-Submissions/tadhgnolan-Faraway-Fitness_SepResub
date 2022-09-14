from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from memberships.models import Membership
from bag.contexts import bag_contents


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LN9XuFK3uJBUiyjeJMFsrpzJPOeHNFWOuI8RZ3Vku9uxT2UCaJvnBv8sXjAb6eB8ZVP0iPQstLj0KBOIWVQDxuH00BLxGwJTj',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
