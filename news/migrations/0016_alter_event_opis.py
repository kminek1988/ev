# Generated by Django 4.0.6 on 2022-07-19 17:37

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_alter_event_opis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='opis',
            field=djrichtextfield.models.RichTextField(blank=True, null=True),
        ),
    ]
