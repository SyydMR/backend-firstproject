# Generated by Django 3.2.2 on 2024-01-09 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20240109_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination_city',
            name='cost',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='destination_city',
            name='transportation',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.transportation'),
        ),
    ]
