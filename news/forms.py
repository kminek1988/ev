from django import forms  
from django.contrib.auth.models import User  
from acc.models import Profil
from .models import Event
class event_add(forms.ModelForm):
    class Meta:
        model = Profil
        fields = [
            'event'
        ]
        exclude = [
            'user', 'nanme', 'surname', 'tel', 'email', 'organizator', 'wystawca', 'administrator', 'img',
            'rodzaj', 'region','img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'logo', 'sex', 'adres', 'miasto',
        ]