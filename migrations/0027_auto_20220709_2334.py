# Generated by Django 3.1.5 on 2022-07-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0026_auto_20220709_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Quiz1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Quiz2',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Quiz3',
            field=models.BooleanField(default=False),
        ),
    ]
