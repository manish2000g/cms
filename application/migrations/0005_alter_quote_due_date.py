# Generated by Django 4.2.4 on 2023-09-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_applicant_documents_alter_payment_applicant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='due_date',
            field=models.DateField(blank=True),
        ),
    ]
