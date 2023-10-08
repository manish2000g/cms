# Generated by Django 4.2.4 on 2023-09-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_englishprofficiency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='min_english_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='min_gpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]
