# Generated by Django 4.0.6 on 2022-07-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferencje', '0002_alter_rodzaj_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodzaj',
            name='img',
            field=models.ImageField(blank=True, default='media/1.png', null=True, upload_to='media/rodzaje', verbose_name='awatar, 300x400'),
        ),
    ]
