# Generated by Django 4.2.3 on 2023-08-14 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classschedule',
            name='duration',
        ),
    ]