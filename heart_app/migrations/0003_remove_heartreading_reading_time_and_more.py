# Generated by Django 5.1.5 on 2025-01-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_app', '0002_heartreading_reading_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heartreading',
            name='reading_time',
        ),
        migrations.AlterField(
            model_name='heartreading',
            name='reading_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]