# Generated by Django 4.1.5 on 2023-03-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_image_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_src',
            name='image_scr',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
