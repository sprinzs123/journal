# Generated by Django 4.1 on 2022-12-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_rename_date_entry_date_end_entry_date_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='day_of_week_end',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='entry',
            name='tags',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]