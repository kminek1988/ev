
from django.http import HttpResponse  
from django.shortcuts import render, redirect , get_object_or_404 

from django.urls import reverse
from .forms import SignupForm, preferencje_createForm, region_createForm 
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, CreateView

from acc.models import Profil
from preferencje.models import Region, Miasto, Rodzaj
from news.models import Event
from django.views.generic import DetailView
from .forms import region_createForm, miasto_createForm, profilUpdate
from django.db.models import Q








def sukces(request):
    return render (request, 'sukces/sukces.html')




def signup(request):  
    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'eventinfo.pl przesyła link aktywacyjny'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return redirect('confirmation') 
    else:  
        form = SignupForm()  
    return render(request, 'signup.html', {'form': form})  


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('sukces') 
    else:  
        return HttpResponse('Activation link is invalid!')  


def confirmation(request):
    return render (request, 'confirmation.html')
def profil (request, pk=None):
    user = request.user
    pr = Profil.objects.get(user=user)
    imprezy = pr.event.all()
    user_region = pr.region.all()
    user_miasto = pr.miasto.all()
    user_preferencje = pr.rodzaj.all()
    wg_miasta = Event.objects.filter(id__in=user_miasto)
    wg_zainteresowan = Event.objects.filter(id__in=user_preferencje)
    najlepsze = Event.objects.filter(Q(id__in=user_miasto) & Q(id__in=user_preferencje))
    if request.method == 'POST':
        usun =  request.POST.get('usun')
        impr = pr.event.get(id=usun)
        pr.event.remove(impr)
        

        

    context = {
        'pr' : pr,
        'imprezy': imprezy,
        'user_region': user_region,
        'user_miasto': user_miasto,
        'user_preferencje': user_preferencje,
        'wg_miasta': wg_miasta,
        'wg_zainteresowan': wg_zainteresowan,
        'najlepsze': najlepsze

    }
    return render(request, 'acc/profil_temp.html', context)





class create_region(LoginRequiredMixin, UpdateView):
    model = Profil
    form_class = region_createForm
    template_name = 'create/regions.html'
    def get_success_url(self):
        return 'create-miasto'
class create_miasto(LoginRequiredMixin, UpdateView):
    model = Profil
    form_class = miasto_createForm
    template_name = 'create/create_miasto.html'
    def get_success_url(self):
        return 'create-preferencje'

class create_preferencje( LoginRequiredMixin, UpdateView):
    model = Profil
    form_class = preferencje_createForm
    template_name = 'create/create_preferencje.html'
    def get_success_url(self):
       return reverse("profil", kwargs={'pk': self.object.pk})
class ProfilUpdate(LoginRequiredMixin, UpdateView):
    model = Profil
    form_class = profilUpdate
    template_name = 'acc/update.html'
    def get_success_url(self):
       return reverse("profil", kwargs={'pk': self.object.pk})


