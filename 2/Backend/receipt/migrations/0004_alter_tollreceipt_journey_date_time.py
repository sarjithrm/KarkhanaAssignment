# Generated by Django 3.2.3 on 2021-05-21 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0003_auto_20210521_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tollreceipt',
            name='journey_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 21, 15, 23, 58, 338440)),
        ),
    ]
