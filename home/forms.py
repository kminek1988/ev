from django import forms
from .models import Formularz

class formularzForm(forms.ModelForm):
    class Meta:
        model = Formularz
        fields = '__all__'

    # def send_email(self):

        