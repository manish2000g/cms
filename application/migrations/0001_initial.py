# Generated by Django 4.2.3 on 2023-08-09 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_purpose', models.CharField(choices=[('Inquiring', 'Inquiring'), ('Class Enrollment', 'Class Enrollment'), ('Abroad Enrollment', 'Abroad Enrollment')], max_length=30)),
                ('status', models.CharField(choices=[('Interested', 'Interested'), ('Created', 'Created'), ('Submitted', 'Submitted'), ('Offer', 'Offer'), ('Visa Created', 'Visa Created'), ('Visa Submitted', 'Visa Submitted'), ('Docs Requested', 'Docs Requested'), ('Granted', 'Granted'), ('Rejected', 'Rejected'), ('Enrolled', 'Enrolled')], default='Interested', max_length=20)),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('institution', models.CharField(max_length=200)),
                ('degree_title', models.CharField(max_length=150)),
                ('degree_level', models.CharField(max_length=50)),
                ('passed_year', models.DateField()),
                ('course_start_date', models.DateField()),
                ('course_end_date', models.DateField()),
                ('academic_score_category', models.CharField(choices=[('Percentage', 'Percentage'), ('GPA', 'GPA')], max_length=20)),
                ('academic_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('address', models.CharField(max_length=150)),
                ('ielts_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('toefl_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('pte_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('gre_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('gmat_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sat_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('other_language', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('file', models.FileField(upload_to='applicant_documents/')),
            ],
        ),
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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.applicant')),
            ],
        ),
        migrations.AddField(
            model_name='applicant',
            name='documents',
            field=models.ManyToManyField(to='application.document'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='interested_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.country'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='interested_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.course'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='interested_institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.institution'),
        ),
    ]
