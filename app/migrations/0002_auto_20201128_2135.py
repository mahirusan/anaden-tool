# Generated by Django 3.1.3 on 2020-11-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintask',
            name='task_seq',
            field=models.IntegerField(blank=True, null=True, verbose_name='順序'),
        ),
        migrations.AddField(
            model_name='subtask',
            name='task_seq',
            field=models.IntegerField(blank=True, null=True, verbose_name='順序'),
        ),
    ]