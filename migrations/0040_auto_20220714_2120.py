# Generated by Django 3.1.5 on 2022-07-15 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0039_auto_20220714_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Ques_No',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
