# Generated by Django 3.1.5 on 2022-06-20 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0018_auto_20220619_1557'),
        ('quiz', '0004_auto_20220619_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('Ques_No', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('Ques', models.CharField(max_length=1000)),
                ('Option_1', models.CharField(max_length=500)),
                ('Option_2', models.CharField(max_length=500)),
                ('Option_3', models.CharField(max_length=500)),
                ('Option_4', models.CharField(max_length=500)),
                ('Correct_Option', models.CharField(max_length=500)),
                ('Answer_Description', models.TextField(max_length=1000)),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.training')),
            ],
        ),
    ]
