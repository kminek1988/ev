from django.shortcuts import redirect
from .models import Formularz
from .forms import formularzForm
from django.shortcuts import  redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError, EmailMessage, get_connection
from django.core.mail import send_mail

def formularz(request):
    return {
        'formularz': formularzForm()
    }
