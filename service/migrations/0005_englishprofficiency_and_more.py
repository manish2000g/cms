# Generated by Django 4.2.4 on 2023-09-26 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_institution_english_profficiency_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishProfficiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_profficiency', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='institution',
            name='english_profficiency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='english_score', to='service.englishprofficiency'),
        ),
    ]
