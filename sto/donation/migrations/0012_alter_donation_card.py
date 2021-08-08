# Generated by Django 3.2.5 on 2021-08-07 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0011_alter_donation_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='card',
            field=models.CharField(choices=[('hana', '하나'), ('woori', '우리'), ('kB', '국민'), ('shinhan', '신한')], max_length=10, verbose_name='카드사'),
        ),
    ]