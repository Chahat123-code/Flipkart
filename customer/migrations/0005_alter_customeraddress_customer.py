# Generated by Django 4.2.1 on 2023-05-30 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_customeradhar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_address', to='customer.customers'),
        ),
    ]
