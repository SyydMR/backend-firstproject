# Generated by Django 3.2.23 on 2024-01-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20240105_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='date_destination',
        ),
        migrations.AddField(
            model_name='invoice',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
