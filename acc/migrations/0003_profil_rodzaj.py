# Generated by Django 4.0.6 on 2022-07-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferencje', '0001_initial'),
        ('acc', '0002_profil_miasto_profil_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='rodzaj',
            field=models.ManyToManyField(blank=True, to='preferencje.rodzaj'),
        ),
    ]
