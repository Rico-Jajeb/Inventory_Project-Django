# Generated by Django 4.1.4 on 2023-01-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_case_items_db_cpu_fan_items_db_headphone_items_db_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transac_date', models.DateField()),
                ('unit', models.CharField(max_length=100)),
                ('total_cost', models.IntegerField()),
                ('transac_person', models.CharField(max_length=100)),
                ('reference_no', models.CharField(max_length=100)),
            ],
        ),
    ]
