# Generated by Django 4.2.4 on 2023-09-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_alter_institution_min_english_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='min_english_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='min_gpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
