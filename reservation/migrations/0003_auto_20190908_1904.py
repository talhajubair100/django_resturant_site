# Generated by Django 2.2.4 on 2019-09-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20190831_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='time',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
