# Generated by Django 4.1.5 on 2023-03-03 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0020_delete_video_remove_faculty_university_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_src',
            name='first',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='image_src',
            name='second',
            field=models.BooleanField(default=True),
        ),
    ]
