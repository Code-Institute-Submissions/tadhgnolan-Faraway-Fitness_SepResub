from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from memberships.models import Membership


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Membership, pk=item_id)
        sub_total = quantity * product.price
        total += sub_total
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'sub_total': sub_total,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_count': product_count,
        'grand_total': grand_total,
    }

    return context
