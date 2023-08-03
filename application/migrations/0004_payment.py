# Generated by Django 4.2.3 on 2023-08-03 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_document_remove_applicant_documents_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('grand_total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remaining_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20)),
                ('action', models.CharField(max_length=255)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.applicant')),
            ],
        ),
    ]
