# Generated by Django 3.2.8 on 2021-10-11 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='users',
            field=models.ManyToManyField(help_text='Users who are connected to the classroom', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
