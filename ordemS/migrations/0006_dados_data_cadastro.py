# Generated by Django 4.2 on 2023-07-16 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ordemS', '0005_dados_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
