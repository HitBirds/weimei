# Generated by Django 2.0.3 on 2018-04-26 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0008_auto_20180426_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothes',
            name='color',
        ),
        migrations.RemoveField(
            model_name='clothes',
            name='colorImg',
        ),
    ]
