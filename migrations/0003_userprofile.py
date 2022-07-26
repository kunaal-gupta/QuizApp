# Generated by Django 3.1.5 on 2022-06-19 23:04

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0018_auto_20220619_1557'),
        ('quiz', '0002_auto_20220619_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('User_Code', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Phone_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Username', models.CharField(help_text='Ignore. Autogenerate by server!', max_length=100)),
                ('Number_of_Quiz', models.IntegerField(default=1)),
                ('Program_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserProfile', to='training.training')),
            ],
        ),
    ]