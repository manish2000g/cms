# Generated by Django 4.2.3 on 2023-08-20 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_rename_status_event_event_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='tag_name',
        ),
    ]
