# Generated by Django 5.1.5 on 2025-01-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_app', '0003_remove_heartreading_reading_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartreading',
            name='reading_date',
            field=models.DateTimeField(),
        ),
    ]
