# Generated by Django 3.2.13 on 2022-06-06 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0004_alter_user_model_usergroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
