# Generated by Django 3.1.4 on 2021-03-02 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='summery',
            new_name='summary',
        ),
    ]
