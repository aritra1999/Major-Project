# Generated by Django 3.2.8 on 2021-10-15 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_auto_20211015_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='users',
        ),
    ]
