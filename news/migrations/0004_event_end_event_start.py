# Generated by Django 4.0.6 on 2022-07-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_event_bg'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start',
            field=models.DateField(null=True),
        ),
    ]
