# Generated by Django 4.1 on 2022-08-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_support_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.PositiveIntegerField(default=1),
        ),
    ]