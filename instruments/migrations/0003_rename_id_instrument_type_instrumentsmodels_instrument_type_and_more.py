# Generated by Django 4.2.2 on 2023-09-08 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0002_remove_instrumentsmodels_expressions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instrumentsmodels',
            old_name='id_instrument_type',
            new_name='instrument_type',
        ),
        migrations.AlterField(
            model_name='instrumentsmodels',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
