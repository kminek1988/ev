# Generated by Django 4.0.6 on 2022-07-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_event_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='panstwo',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
