# Generated by Django 4.2.3 on 2023-08-21 10:15

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='major_city',
        ),
        migrations.RemoveField(
            model_name='country',
            name='visa_requirements',
        ),
        migrations.RemoveField(
            model_name='course',
            name='application_deadline',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_end_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_image',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_start_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_website',
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='country',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='service.country'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='courses',
            field=models.ManyToManyField(related_name='courses', to='service.course'),
        ),
    ]