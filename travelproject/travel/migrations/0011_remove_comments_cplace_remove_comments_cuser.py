# Generated by Django 4.1.2 on 2023-06-07 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='cplace',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='cuser',
        ),
    ]
