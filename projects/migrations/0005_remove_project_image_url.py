# Generated by Django 4.2.8 on 2023-12-09 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image_url',
        ),
    ]
