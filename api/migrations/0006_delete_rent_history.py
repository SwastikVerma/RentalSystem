# Generated by Django 5.0.6 on 2024-07-02 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_carmodel_car_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rent_history',
        ),
    ]
