# Generated by Django 4.2.4 on 2023-09-20 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_alter_payment_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_payment', to='application.applicant'),
        ),
    ]
