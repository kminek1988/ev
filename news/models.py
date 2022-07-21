from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from preferencje.models import Region, Miasto, Rodzaj

from django.urls import reverse


class Event (models.Model):
    name = models.CharField(max_length=500, blank=True,
                            null=True, verbose_name="nazwa wydarzenia")
    short = models.TextField(null=True, blank=True, verbose_name="krótki opis")
    opis =   RichTextUploadingField(null=True, blank=True, config_name='default')
    plakat = models.ImageField(upload_to='media/event', null=True, blank=True)
    region = models.ForeignKey(
        Region, on_delete=models.DO_NOTHING, null=True, blank=True)
    miasto = models.ForeignKey(
        Miasto, on_delete=models.DO_NOTHING, null=True, blank=True)
    rodzaj = models.ForeignKey(
        Rodzaj, on_delete=models.DO_NOTHING, null=True, blank=True)
    bg = models.ImageField(upload_to='media/event/bgs',
                           blank=True, null=True, default='media/1.png')
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True , blank=True)
    archiwum = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name='utworzono')
    adres = RichTextUploadingField(null=True, blank=True)
    mapa = models.CharField(max_length=2000, null=True, blank=True)
    w = models.CharField(max_length=255, null=True, blank=True, verbose_name="do odmiany")
    


    class Meta:
        verbose_name = 'wydarzenie'
        verbose_name_plural = "wydarzenia"

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('event', args=[str(self.id)])
