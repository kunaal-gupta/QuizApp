# Generated by Django 3.1.5 on 2022-07-15 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0041_auto_20220714_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Ques_No',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]