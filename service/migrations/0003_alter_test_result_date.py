# Generated by Django 4.2.4 on 2023-09-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_classschedule_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='result_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
