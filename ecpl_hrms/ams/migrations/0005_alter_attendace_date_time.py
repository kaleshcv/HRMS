# Generated by Django 3.2.7 on 2021-09-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0004_alter_attendace_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendace',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
