

from email.policy import default
from django.db import models

from django.urls import reverse
# Create your models here.


class Region (models.Model):
    name = models.CharField(max_length=255, null=True,
                            blank=True, verbose_name='nazwa')

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiony"

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('region', args=[str(self.id)])


class Miasto(models.Model):

    name = models.CharField(max_length=255, null=True,
                            blank=True, verbose_name="nazwa")
    region = models.ForeignKey(
        Region, null=True, blank=True, on_delete=models.DO_NOTHING)
    

    class Meta:
        verbose_name = 'Miasto'
        verbose_name_plural = "Miasta"

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('miasto', args=[str(self.id)])


class Rodzaj (models.Model):
    name = models.CharField(max_length=255, null=True,
                            blank=True, verbose_name='nazwa')
    img = models.ImageField(upload_to='media/rodzaje',
                            null=True, blank=True, verbose_name="awatar, 300x400", default='media/1.png')
    opis = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Rodzaj'
        verbose_name_plural = 'Rodzaje'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('rodzaj', args=[str(self.id)])
