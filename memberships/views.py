from django.shortcuts import render
from django.http import HttpResponse
from .models import MembershipType

# Create your views here.


"""def memberships(request):
    """ A view to return the member page """

    return render(request=request, 
                  template_name='memberships/member.html',
                  context=['members':MembershipType.objects.all]) """