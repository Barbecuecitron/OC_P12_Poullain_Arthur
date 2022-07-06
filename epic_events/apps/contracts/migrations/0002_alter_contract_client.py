# Generated by Django 3.2.13 on 2022-07-06 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
            preserve_default=False,
        ),
    ]
