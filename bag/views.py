from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from memberships.models import Membership

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, membership_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Membership, pk=membership_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    if membership_id in list(bag.keys()):
        bag[membership_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[membership_id]}')
    else:
        bag[membership_id] = quantity
        messages.success(request, f'Added {product.title} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, membership_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Membership, pk=membership_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[membership_id] = quantity
        messages.success(request, f'Updated {product.title} quantity to {bag[membership_id]}')
    else:
        bag.pop(membership_id)
        messages.success(request, f'Removed {product.title} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, membership_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Membership, pk=membership_id)
        bag = request.session.get('bag', {})
        bag.pop(membership_id)
        messages.success(request, f'Removed {product.title} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
