from django.db import models

# Create your models here.
class Formularz(models.Model):
    TEMAT = [ 
        ('Event', 'Event'),
        ('Wystawca', 'Wystawca'),
        ('Organizacja', 'Organizacja'),
        ('Inne', 'Inne'),
    ]
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='imię')
    surname = models.CharField(max_length=255, null=True, blank=True, verbose_name='nazwisko')
    tel = models.IntegerField(null=True, blank=True)
    choice = models.CharField(choices=TEMAT, blank=False, null=True, verbose_name='wybór', max_length=500)
    temat = models.CharField(max_length=1000, null=True, blank=True)
    content = models.TextField(null=True, blank=True, verbose_name='treść wiadomości')
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'wiadomość formularza'
        verbose_name_plural = 'wiadomości formularza'


    def __str__(self):
        return f'{self.temat} { self.email }'


    
