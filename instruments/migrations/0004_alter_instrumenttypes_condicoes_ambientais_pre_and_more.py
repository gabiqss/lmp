# Generated by Django 4.2.2 on 2023-11-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0003_rename_id_instrument_type_instrumentsmodels_instrument_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumenttypes',
            name='condicoes_ambientais_pre',
            field=models.CharField(default=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='instrumenttypes',
            name='condicoes_ambientais_temp',
            field=models.CharField(default=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='instrumenttypes',
            name='condicoes_ambientais_umi',
            field=models.CharField(default=False, max_length=5),
        ),
    ]