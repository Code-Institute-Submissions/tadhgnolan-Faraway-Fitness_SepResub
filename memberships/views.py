from django.shortcuts import render
from .models import Membership_type

# Create your views here.

def all_memberships(request):
        """A view to show3 all product, including sorting and search queries"""

        memberships = Memberships.objects.all()

        context = {
            'memberships': memberships,
        }

        return render(request, 'memberships/memberships.html', context)        