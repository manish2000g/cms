# Generated by Django 4.2.3 on 2023-08-26 09:23

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=10)),
                ('class_name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('price', models.PositiveIntegerField()),
                ('max_capacity', models.PositiveIntegerField()),
                ('instructor', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('course_start_date', models.DateField()),
                ('course_end_date', models.DateField()),
                ('application_deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('location', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField()),
                ('event_status', models.CharField(choices=[('Upcoming', 'Upcoming'), ('Ongoing', 'Ongoing'), ('Past', 'Past')], default='Upcoming', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Counseling', 'Counseling'), ('Visa Processing', 'Visa Processing'), ('Admission Assistance', 'Admission Assistance'), ('Scholarship Guidance', 'Scholarship Guidance'), ('Test Preparation', 'Test Preparation'), ('Document Verification', 'Document Verification'), ('Interview Preparation', 'Interview Preparation'), ('Application Review', 'Application Review'), ('Career Counseling', 'Career Counseling')], max_length=100)),
                ('description', models.TextField()),
                ('duration', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('test_date', models.DateField()),
                ('test_time', models.TimeField()),
                ('max_capacity', models.PositiveIntegerField()),
                ('result_date', models.DateField()),
                ('test_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_type', to='service.classschedule')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=255, unique=True)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='service.country')),
                ('courses', models.ManyToManyField(related_name='courses', to='service.course')),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('preferred_country', models.CharField(max_length=100)),
                ('preferred_course', models.CharField(max_length=255)),
                ('date_of_enquiry', models.DateField()),
                ('enquiry_type', models.CharField(choices=[('General', 'General Inquiry'), ('Visa', 'Visa Inquiry'), ('Course', 'Course Inquiry')], max_length=20)),
                ('enquiry_status', models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Closed', 'Closed')], default='Open', max_length=20)),
                ('preferred_institution', models.CharField(blank=True, max_length=200, null=True)),
                ('enquiry_assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='degree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='degree', to='service.coursetype'),
        ),
    ]
