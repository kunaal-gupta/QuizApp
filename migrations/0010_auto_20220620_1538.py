# Generated by Django 3.1.5 on 2022-06-20 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0009_auto_20220620_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='First_Name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Last_Name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='User_Identity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]