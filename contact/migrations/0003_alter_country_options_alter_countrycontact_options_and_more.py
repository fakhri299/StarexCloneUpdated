# Generated by Django 4.1.4 on 2022-12-24 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_countrycontact_first_day_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Ölkələr'},
        ),
        migrations.AlterModelOptions(
            name='countrycontact',
            options={'verbose_name_plural': 'Ölkə kontaktları'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name_plural': 'Rayonlar'},
        ),
        migrations.AlterModelOptions(
            name='pointcontact',
            options={'verbose_name_plural': 'Məntəqələr'},
        ),
    ]
