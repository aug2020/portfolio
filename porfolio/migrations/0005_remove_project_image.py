# Generated by Django 3.0.8 on 2020-08-17 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0004_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]