# Generated by Django 4.1 on 2022-12-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_alter_entry_day_of_week_end_alter_entry_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_end',
            field=models.DateField(blank=True),
        ),
    ]