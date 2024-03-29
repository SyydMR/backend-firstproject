# Generated by Django 3.2.2 on 2024-01-09 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_invoice_city_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination_City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.city')),
                ('destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.destination')),
            ],
        ),
    ]
