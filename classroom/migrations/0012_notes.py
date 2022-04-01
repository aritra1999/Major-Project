# Generated by Django 3.2.8 on 2022-03-31 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0011_alter_classroom_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.CharField(blank=True, max_length=1000, null=True)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom')),
            ],
        ),
    ]