# Generated by Django 4.1.2 on 2023-06-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0029_remove_comments_cimage_comments_ctext_imagereview'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='cdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
