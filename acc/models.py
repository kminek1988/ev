
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db.models.signals import post_save
from django.urls import reverse
from preferencje.models import Rodzaj, Miasto, Region
from news.models import Event
# Create your models here.
User._meta.get_field('email')._unique = True


class Profil(models.Model):
    SEX = [ 
        ('żeńska', 'żeńska'),
        ('męska', 'męska'),
    ]

    user = models.OneToOneField(User, null=True, blank=False,
                             verbose_name="użytkownik", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255, null=True,
                            blank=True, verbose_name='imię')
    surname = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='nazwisko')
    tel = models.IntegerField(null=True, blank=True,
                              verbose_name='numer telefonu')
    email = models.EmailField(null=True, blank=True)
    organizator = models.BooleanField(default=False, null=True, blank=True)
    wystawca = models.BooleanField(default=False, null=True, blank=True)
    administrator = models.BooleanField(default=False, null=True, blank=True)
    img = models.ImageField(upload_to='media/profile/',
                            blank=True, default='media/1.png')
    img1 = models.ImageField(upload_to='media/profile/galeria/',
                            blank=True, default='media/1.png')
    img2 = models.ImageField(upload_to='media/profile/galeria/',
                            blank=True, default='media/1.png')
    img3 = models.ImageField(upload_to='media/profile/galeria/',
                            blank=True, default='media/1.png')
    img4 = models.ImageField(upload_to='media/profile/galeria/',
                            blank=True, default='media/1.png')
    img5 = models.ImageField(upload_to='media/profile/galeria/',
                            blank=True, default='media/1.png')
    img6 = models.ImageField(upload_to='media/profile/galeria/',
                            blank=True, default='media/1.png')
    rodzaj = models.ManyToManyField(Rodzaj, blank=True)
    miasto = models.ManyToManyField(Miasto, blank=True)
    region = models.ManyToManyField(Region, blank=True)
    event = models.ManyToManyField(Event, blank=True, verbose_name="wydarzenie")
    adres = models.TextField(blank=True, null=True, verbose_name='adres firmy')
    logo = models.ImageField(upload_to="media/profile/loga/", blank=True, null=True)
    sex = models.CharField(max_length=255, choices=SEX, verbose_name='płeć', null=True)
    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse('profil', args=[str(self.id)])

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profil.objects.create(user=instance, email=instance.email)
            instance.profil.save()
