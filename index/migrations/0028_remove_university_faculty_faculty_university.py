# Generated by Django 4.1.5 on 2023-03-06 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0027_remove_university_faculty_university_faculty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='faculty',
        ),
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.university'),
        ),
    ]
