# Generated by Django 4.1.5 on 2023-03-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_remove_bookdb_b_password_bookdb_b_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdb',
            name='status',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
