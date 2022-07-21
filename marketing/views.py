from multiprocessing import context
from django.shortcuts import render
from acc.models import Profil
from news.models import Event
from preferencje.models import Region, Rodzaj, Miasto
# Create your views here.
def Dashboard(request):
    profile_all = Profil.objects.all()
    context = {
        'profile_all':profile_all,
    }
    return render (request, 'marketing/dash.html', context)