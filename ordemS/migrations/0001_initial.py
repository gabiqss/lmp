# Generated by Django 4.2 on 2023-05-29 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=100)),
                ('contato', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('fone', models.CharField(max_length=20)),
                ('cnpj', models.CharField(max_length=20)),
                ('data_entrada', models.DateField()),
                ('saida_prevista', models.DateField()),
                ('contrato', models.CharField(max_length=100)),
                ('data_chamado', models.DateField()),
                ('data_atendimento', models.DateField()),
                ('cep', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=20)),
                ('nota_fiscal', models.CharField(max_length=100)),
                ('tipo_envio', models.CharField(max_length=100)),
                ('embalagem', models.CharField(max_length=100)),
                ('info_instrumentos', models.TextField()),
                ('observacoes', models.TextField()),
            ],
        ),
    ]
