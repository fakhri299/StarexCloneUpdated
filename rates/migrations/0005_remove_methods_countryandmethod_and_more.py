# Generated by Django 4.1.4 on 2022-12-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0004_methods_countryandmethod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='methods',
            name='countryandmethod',
        ),
        migrations.AddField(
            model_name='tarif',
            name='countryandmethod',
            field=models.CharField(max_length=100, null=True),
        ),
    ]