# Generated by Django 4.2 on 2023-06-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts_customers',
            name='cellular',
            field=models.CharField(blank=True, default=' ', max_length=250),
        ),
        migrations.AlterField(
            model_name='contacts_customers',
            name='commercial_phone',
            field=models.CharField(blank=True, default=' ', max_length=250),
        ),
        migrations.AlterField(
            model_name='contacts_customers',
            name='cpf',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacts_customers',
            name='description',
            field=models.CharField(blank=True, default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='contacts_customers',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacts_customers',
            name='name',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacts_customers',
            name='sector',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]