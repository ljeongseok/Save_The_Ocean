# Generated by Django 3.2.5 on 2021-08-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0005_auto_20210809_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funding',
            name='product',
        ),
        migrations.AddField(
            model_name='funding',
            name='num',
            field=models.IntegerField(default=1),
        ),
    ]
