# Generated by Django 4.2.2 on 2024-01-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_customers_main_tipo_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts_customers',
            name='cpf',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='customers_main',
            name='address_complement',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]