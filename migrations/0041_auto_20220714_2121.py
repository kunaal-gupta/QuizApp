# Generated by Django 3.1.5 on 2022-07-15 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0040_auto_20220714_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Ques_No',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
