# Generated by Django 4.1.4 on 2023-01-06 18:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='increasebalance',
            name='card_number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(16)]),
        ),
        migrations.AlterField(
            model_name='increasebalance',
            name='day_month',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(4), django.core.validators.MinLengthValidator(2)]),
        ),
    ]