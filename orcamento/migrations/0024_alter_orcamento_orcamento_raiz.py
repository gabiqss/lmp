# Generated by Django 4.2.2 on 2024-03-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0023_alter_orcamento_orcamento_raiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='orcamento_raiz',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]