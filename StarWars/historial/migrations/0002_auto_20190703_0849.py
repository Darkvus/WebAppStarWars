# Generated by Django 2.2.2 on 2019-07-03 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 3, 8, 49, 53, 616686)),
        ),
    ]