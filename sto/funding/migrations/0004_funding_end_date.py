# Generated by Django 3.2.5 on 2021-08-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0003_rename_porduct_funding_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='funding',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
