# Generated by Django 5.0.6 on 2024-05-21 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_customer_address_remove_customer_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_adult',
        ),
    ]
