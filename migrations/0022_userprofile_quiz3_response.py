# Generated by Django 3.1.5 on 2022-07-10 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0021_userprofile_quiz2_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Quiz3_response',
            field=models.TextField(default='', null=True),
        ),
    ]
