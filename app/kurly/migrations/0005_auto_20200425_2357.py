# Generated by Django 2.2.11 on 2020-04-25 14:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kurly', '0004_auto_20200416_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_bk',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='image_pp',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
