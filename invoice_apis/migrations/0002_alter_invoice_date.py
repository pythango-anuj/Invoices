# Generated by Django 5.0.1 on 2024-01-24 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 1, 24, 10, 35, 37, 392513), verbose_name='Date'),
        ),
    ]