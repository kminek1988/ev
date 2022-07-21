from tabnanny import verbose
from django.db import models
from datetime import datetime
from django.dispatch import receiver
from news.models import Event
from django.db.models.signals import post_save
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=1000, verbose_name='nazwa')
    event = models.ForeignKey(
        Event, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = 'forum'
        verbose_name_plural = 'fora'

    def __str__(self):
        return f'{self.name}'

    @receiver(post_save, sender=Event)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            room = Room.objects.create(event=instance, name=instance.name)
            room.save()


class Message(models.Model):
    value = models.CharField(max_length=1000000, verbose_name='treść')
    date = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name='data')
    user = models.CharField(max_length=1000000, verbose_name='użytkownik')
    room = models.CharField(max_length=1000000, verbose_name='forum')

    class Meta:
        verbose_name = 'widomość'
        verbose_name_plural = 'wiadomości'

    def __str__(self):
        return f'{self.room} {self.user}'
