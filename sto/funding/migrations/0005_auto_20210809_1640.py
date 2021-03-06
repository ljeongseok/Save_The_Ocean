# Generated by Django 3.2.5 on 2021-08-09 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0004_funding_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('goal_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='funding',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='goal_price',
        ),
        migrations.AddField(
            model_name='funding',
            name='funding_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='funding.fundinginfo', verbose_name='Funding Info.'),
        ),
    ]
