# Generated by Django 4.1.2 on 2023-06-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_remove_place_main_image_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, upload_to='gallery'),
        ),
    ]
