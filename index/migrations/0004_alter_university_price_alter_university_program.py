# Generated by Django 4.1.5 on 2023-02-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_rename_university_id_faculty_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='university',
            name='program',
            field=models.CharField(max_length=200),
        ),
    ]
