# Generated by Django 4.2.4 on 2023-09-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_quote_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
