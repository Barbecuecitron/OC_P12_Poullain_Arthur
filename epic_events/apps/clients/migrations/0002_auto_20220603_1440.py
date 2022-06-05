# Generated by Django 3.2.13 on 2022-06-03 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0004_alter_user_model_usergroup'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(blank=True, limit_choices_to={'usergroup': 'Sale'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management.user_model'),
        ),
    ]