# Generated by Django 4.2.3 on 2023-08-23 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(blank=True, choices=[('Created', 'Created'), ('Submitted', 'Submitted'), ('Confirmed', 'Confirmed'), ('Visa_Created', 'Visa_Created'), ('Visa_Submitted', 'Visa_Submitted'), ('Docs_Requested', 'Docs_Requested'), ('Granted', 'Granted'), ('Enrolled', 'Enrolled')], default='Created', max_length=20, null=True),
        ),
    ]
