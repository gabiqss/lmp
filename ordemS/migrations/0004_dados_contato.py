# Generated by Django 4.2 on 2023-07-16 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordemS', '0003_remove_dados_contato'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados',
            name='contato',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
