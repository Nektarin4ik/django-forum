# Generated by Django 3.2.15 on 2023-01-23 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20230124_0214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentsanime',
            name='rating',
        ),
    ]
