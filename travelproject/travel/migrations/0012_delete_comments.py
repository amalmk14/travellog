# Generated by Django 4.1.2 on 2023-06-07 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0011_remove_comments_cplace_remove_comments_cuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
