# Generated by Django 5.0.10 on 2024-12-19 12:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_alter_driver_email_alter_driver_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='rent_date',
        ),
        migrations.AddField(
            model_name='rental',
            name='rent_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='rental',
            name='comments',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
