# Generated by Django 4.1.2 on 2023-06-08 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0022_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
