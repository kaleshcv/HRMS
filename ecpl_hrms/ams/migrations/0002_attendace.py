# Generated by Django 3.2.7 on 2021-09-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(unique=True)),
                ('emp_name', models.CharField(max_length=300)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('process', models.CharField(max_length=300)),
                ('marked_by_id', models.IntegerField()),
                ('marked_by_name', models.CharField(max_length=300)),
                ('attendance_type', models.CharField(max_length=100)),
                ('remarks', models.TextField()),
            ],
        ),
    ]
