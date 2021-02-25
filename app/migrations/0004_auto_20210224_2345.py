# Generated by Django 3.1.3 on 2021-02-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210214_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintask',
            name='types',
            field=models.IntegerField(choices=[(1, 'メインストーリー'), (2, '外典'), (3, '外伝'), (4, '邂逅'), (5, '断章'), (6, '協奏'), (7, 'オリジナルタスク'), (8, 'その他')], verbose_name='タイプ'),
        ),
    ]