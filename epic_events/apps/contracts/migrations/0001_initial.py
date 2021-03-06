# Generated by Django 3.2.13 on 2022-06-19 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField()),
                ('payment_due', models.DateTimeField()),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('SIGNED', 'Contract Signed'), ('ENDED', 'Ended')], default='OPEN', max_length=32)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.client')),
                ('sales_contact', models.ForeignKey(blank=True, limit_choices_to={'usergroup': 'Sale'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
