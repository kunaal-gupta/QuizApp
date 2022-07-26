# Generated by Django 3.1.5 on 2022-07-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0047_auto_20220718_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='Instruction',
            field=models.TextField(default='No instructions for this quiz', help_text='Enter Quiz instructions for this training '),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='file',
            field=models.FileField(default='training_name.csv', help_text='Upload CSV file as training_name.csv. Eg PMP.csv', upload_to=''),
        ),
    ]
