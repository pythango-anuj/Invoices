# Generated by Django 5.0.1 on 2024-01-24 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_apis', '0002_alter_invoice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Date'),
        ),
    ]