# Generated by Django 3.1.5 on 2022-07-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0051_auto_20220718_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Number_of_Quiz',
            field=models.IntegerField(default=1, max_length=3),
        ),
    ]
