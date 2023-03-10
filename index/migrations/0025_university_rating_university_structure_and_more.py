# Generated by Django 4.1.5 on 2023-03-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0024_university_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='rating',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='university',
            name='structure',
            field=models.TextField(default=''),
        ),
        migrations.RemoveField(
            model_name='university',
            name='faculty',
        ),
        migrations.AddField(
            model_name='university',
            name='faculty',
            field=models.ManyToManyField(blank=True, null=True, to='index.faculty'),
        ),
    ]
