# Generated by Django 4.2.2 on 2024-02-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0016_alter_servicocalibracao_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicocalibracao',
            name='descricao',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='servicoensaio',
            name='descricao',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='servicomanutencao',
            name='descricao',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='servicoqt',
            name='descricao',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='servicosorcamento',
            name='descricao',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
