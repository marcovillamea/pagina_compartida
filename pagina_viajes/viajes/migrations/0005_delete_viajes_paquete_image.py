# Generated by Django 4.1 on 2022-09-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0004_alter_hotel_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='viajes',
        ),
        migrations.AddField(
            model_name='paquete',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='viajes/'),
        ),
    ]