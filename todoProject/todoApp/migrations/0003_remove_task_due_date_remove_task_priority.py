# Generated by Django 4.2.7 on 2023-11-18 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_task_due_date_task_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='priority',
        ),
    ]
