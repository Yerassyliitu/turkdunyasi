# Generated by Django 4.1.5 on 2023-02-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_university_price_alter_university_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_src',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='university',
            name='images',
        ),
    ]
