# Generated by Django 2.2.12 on 2021-11-07 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_auto_20211107_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='d',
        ),
    ]
