# Generated by Django 4.2.2 on 2024-02-06 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0007_anexosorcamento_servicocalibracao_servicoensaio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='validade_proposta',
            field=models.DateField(blank=True, null=True),
        ),
    ]