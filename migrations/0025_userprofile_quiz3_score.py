# Generated by Django 3.1.5 on 2022-07-10 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0024_auto_20220709_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Quiz3_score',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
