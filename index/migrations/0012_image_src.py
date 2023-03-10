# Generated by Django 4.1.5 on 2023-02-24 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_delete_image_src'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_src',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_scr', models.ImageField(upload_to=None)),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.university')),
            ],
        ),
    ]
