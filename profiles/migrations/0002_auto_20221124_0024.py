# Generated by Django 3.2 on 2022-11-24 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address1',
            new_name='default_address_line1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address2',
            new_name='default_address_line2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_town_or_city',
            new_name='default_city',
        ),
    ]