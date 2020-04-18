# Generated by Django 3.0.5 on 2020-04-18 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plentific_job_number', models.CharField(max_length=7)),
                ('commission_pre_vat', models.FloatField(blank=True, null=True)),
                ('payments', models.FloatField()),
                ('wo_number', models.IntegerField()),
                ('invoice_number', models.IntegerField(blank=True, null=True)),
                ('customer_name', models.CharField(max_length=30)),
                ('job_description', models.TextField()),
            ],
        ),
    ]
