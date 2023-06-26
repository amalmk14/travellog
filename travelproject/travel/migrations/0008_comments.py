# Generated by Django 4.1.2 on 2023-06-06 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0007_delete_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctext', models.TextField(blank=True)),
                ('cimage', models.ImageField(blank=True, upload_to='comment')),
                ('cplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.place')),
                ('cuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
