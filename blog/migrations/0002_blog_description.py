# Generated by Django 4.1.1 on 2022-09-26 23:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
