# Generated by Django 4.0.6 on 2022-07-19 17:36

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_remove_event_mapa_event_adres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='opis',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
