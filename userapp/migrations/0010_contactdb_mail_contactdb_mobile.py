# Generated by Django 4.1.5 on 2023-03-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_contactdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdb',
            name='mail',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='contactdb',
            name='mobile',
            field=models.CharField(default='', max_length=20),
        ),
    ]
