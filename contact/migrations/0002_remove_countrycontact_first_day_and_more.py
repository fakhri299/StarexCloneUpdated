# Generated by Django 4.1.4 on 2022-12-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countrycontact',
            name='first_day',
        ),
        migrations.RemoveField(
            model_name='countrycontact',
            name='first_time',
        ),
        migrations.RemoveField(
            model_name='countrycontact',
            name='last_day',
        ),
        migrations.RemoveField(
            model_name='countrycontact',
            name='last_time',
        ),
        migrations.AddField(
            model_name='countrycontact',
            name='active_period',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
