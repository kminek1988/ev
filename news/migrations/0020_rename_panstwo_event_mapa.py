# Generated by Django 4.0.6 on 2022-07-19 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_alter_event_adres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='panstwo',
            new_name='mapa',
        ),
    ]
