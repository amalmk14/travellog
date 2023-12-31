# Generated by Django 4.1.2 on 2023-06-17 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0028_remove_comments_ctext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='cimage',
        ),
        migrations.AddField(
            model_name='comments',
            name='ctext',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='ImageReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cimage', models.ImageField(blank=True, null=True, upload_to='cimage')),
                ('cplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.place')),
                ('cuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
