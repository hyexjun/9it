# Generated by Django 4.0.2 on 2022-02-18 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_alter_board_b_date_alter_comment_c_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 18, 15, 34, 6, 619587)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='c_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 18, 15, 34, 6, 619587)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='c_pw',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]