from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Membership
from .forms import MembershipForm


def memberships(request):
    """ A view to return the membership page """

    memberships = Membership.objects.all()
    template = 'memberships/memberships.html'
    context = {
        'memberships': memberships,
    }
    return render(request, template, context)


@login_required
def add_membership(request):
    """ A view to return the add membership page """

    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect(reverse('memberships'))

    membership_form = MembershipForm(request.POST or None)
    if request.method == 'POST':
        if membership_form.is_valid():
            membership_form.save()
            messages.success(request, 'Membership Added')
            return redirect(reverse('memberships'))
        messages.error(request, 'Error, Try Again')
    template = 'memberships/add_membership.html'
    context = {
        'membership_form': membership_form,
    }
    return render(request, template, context)


@login_required
def edit_membership(request, membership_id):
    """ A view to return the edit membership page """

    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect(reverse('memberships'))

    membership = get_object_or_404(Membership, id=membership_id)
    membership_form = MembershipForm(request.POST or None, instance=membership)
    if request.method == 'POST':
        if membership_form.is_valid():
            membership_form.save()
            messages.success(request, 'Membership Updated')
            return redirect(reverse('memberships'))
        messages.error(request, 'Error, Try Again')
    template = 'memberships/edit_membership.html'
    context = {
        'membership_form': membership_form,
        'membership': membership,
    }
    return render(request, template, context)


@login_required
def delete_membership(request, membership_id):
    """ A view to return the delete membership page """

    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect(reverse('memberships'))

    membership = get_object_or_404(Membership, id=membership_id)
    membership.delete()
    messages.success(request, 'Membership Deleted')
    return redirect(reverse('memberships'))
