# Generated by Django 4.2.2 on 2024-01-25 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0004_orcamento_responsavel_alter_orcamento_contato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamentopayment',
            name='prazo_entrega',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orcamentopayment',
            name='validade_proposta',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
