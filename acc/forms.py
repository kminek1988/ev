from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from acc.models import Profil
from preferencje.models import Region, Miasto, Rodzaj
  
class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')  


class profilUpdate(forms.ModelForm):
    class Meta:
        model = Profil
        fields = [
        'name', 'surname', 'tel', 'email', 'img', 'sex',
    ]
class region_createForm(forms.ModelForm):
    region= forms.ModelMultipleChoiceField(
        queryset=Region.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Profil
        fields = [
            'region'
        ]
        exclude = [
            'user', 'nanme', 'surname', 'tel', 'email', 'organizator', 'wystawca', 'administrator', 'img',
            'rodzaj', 'miasto',
        ]



class miasto_createForm(forms.ModelForm):
    miasto= forms.ModelMultipleChoiceField(
        queryset=Miasto.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Profil
        fields = [
            'miasto'
        ]
        exclude = [
            'user', 'nanme', 'surname', 'tel', 'email', 'organizator', 'wystawca', 'administrator', 'img',
            'rodzaj', 'region',
        ]
class preferencje_createForm(forms.ModelForm):
    rodzaj= forms.ModelMultipleChoiceField(
        queryset=Rodzaj.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Profil
        fields = [
            'rodzaj'
        ]
        exclude = [
            'user', 'nanme', 'surname', 'tel', 'email', 'organizator', 'wystawca', 'administrator', 'img',
            'miasto', 'region',
        ]