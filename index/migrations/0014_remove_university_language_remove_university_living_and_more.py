# Generated by Django 4.1.5 on 2023-02-25 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_alter_image_src_image_scr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='language',
        ),
        migrations.RemoveField(
            model_name='university',
            name='living',
        ),
        migrations.RemoveField(
            model_name='university',
            name='requirement',
        ),
    ]
