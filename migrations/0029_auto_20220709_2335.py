# Generated by Django 3.1.5 on 2022-07-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0028_auto_20220709_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Quiz1',
            field=models.BooleanField(default=False, verbose_name='Activate Quiz 1'),
        ),
    ]