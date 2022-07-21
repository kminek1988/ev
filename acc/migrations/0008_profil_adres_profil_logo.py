# Generated by Django 4.0.6 on 2022-07-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0007_profil_img1_profil_img2_profil_img3_profil_img4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='adres',
            field=models.TextField(blank=True, null=True, verbose_name='adres firmy'),
        ),
        migrations.AddField(
            model_name='profil',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile/loga/'),
        ),
    ]
