# Generated by Django 3.1.5 on 2022-07-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0037_auto_20220714_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Ques_No',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
