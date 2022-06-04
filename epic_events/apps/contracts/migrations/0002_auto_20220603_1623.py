# Generated by Django 3.2.13 on 2022-06-03 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='phone',
        ),
        migrations.AddField(
            model_name='contract',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='contract',
            name='payment_due',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 16, 23, 14, 997621)),
        ),
    ]
