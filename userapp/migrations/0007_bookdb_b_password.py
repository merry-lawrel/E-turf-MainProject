# Generated by Django 4.1.5 on 2023-03-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_alter_bookdb_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdb',
            name='b_password',
            field=models.CharField(default='', max_length=15),
        ),
    ]