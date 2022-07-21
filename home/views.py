from django.shortcuts import render
from django.views.generic import TemplateView
from news.models import Event
from preferencje.models import Region, Miasto, Rodzaj
from .models import Formularz
from .forms import formularzForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage, get_connection
# Create your views here.


class Home(TemplateView):
    template_name = "home_temp.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_all'] = Event.objects.all().order_by('created_at')[:5]
        context['rodzaje'] = Rodzaj.objects.all()
        return context


class Polityka(TemplateView):
    template_name: "polityka.html"


class Regulamin(TemplateView):
    template_name: 'regulamin.html'


def formularz(request):
   contactmeform = formularzForm(request.POST)


   if request.method == 'POST':
      if contactmeform.is_valid():
       contactmeform.save() # form.save()
      my_host = 'mail.privateemail.com'
      my_port= 587
      my_username = 'faq@obrotni.de'
      my_password = 'polki007'
      my_use_tls = True

      form_detail = Formularz.objects.last()
      message = str(form_detail)
      connection = get_connection(host=my_host,
                                  port=my_port,
                                  username=my_username,
                                  password=my_password,
                                  use_tls=my_use_tls)
      send_mail(
         'Nowe Zapytanie',
         message,
         'faq@obrotni.de',
         ['admin@obrotni.de'],
         connection=connection,
         fail_silently=False,
      )

      return render(request, 'sukces.html')
   else:
      contactmeform = formularzForm(request.POST)
      context = {'formularz': contactmeform}
      return render(request, 'contact.html', context)

           
