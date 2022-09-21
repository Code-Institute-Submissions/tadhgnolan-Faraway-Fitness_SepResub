from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Welcome
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact
from .forms import ContactForm
# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request,
                  template_name='home/index.html',
                  context={'welcomes': Welcome.objects.all})


def contact(request):
    """ A view to return the contact page"""

    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        sender = "Contact request from" + " " + str(email)
        msg_mail = str(message) + ", " + str(sender)
        if form.is_valid():
            send_mail(
                subject,
                msg_mail,
                email,
                [settings.DEFAULT_FROM_EMAIL, ]
            )
            form.save()
            messages.success(request, 'Your message has been delivered.')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request,
                'An error has occured while trying to send your message, please make sure the form is filled out corretly.'
            )
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'home/contact.html', context)
