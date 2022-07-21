from django.views.generic.list import ListView
from datetime import date, datetime, timedelta, time
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView
from news.models import Event
from django.contrib.auth.models import User
from acc.models import Profil
from .forms import event_add

# Create your views here.

def EventView(request, pk):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            profil = request.user.profil
            event_id = request.POST.get('event_id')
            profil.event.add(event_id)     
            profil.save()
            return redirect(request.path)
        else:
            event = get_object_or_404(Event, pk=pk)
            profil = request.user.profil
            profil_event = profil.event.all()
            context =  {
      
            'event': event,
            'profil':profil,
            'profil_event':profil_event
            }
            
        return render(request, 'news/event_detail.html', context)
    else:
        event = get_object_or_404(Event, pk=pk)
        return render(request, 'news/event_detail.html', {'event':event})
    


class EventCalendar(ListView):
    model = Event
    template_name = 'news/kalendarz.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()

        context['calendar'] = Event.objects.filter(start__gte=now).order_by('start')
        context['today'] = Event.objects.filter(start__gte=timezone.now())
    

        return context