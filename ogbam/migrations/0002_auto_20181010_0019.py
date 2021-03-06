# Generated by Django 2.1.2 on 2018-10-10 12:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ogbam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airtime',
            name='amount',
            field=models.CharField(blank=True, choices=[(100, '#100'), (500, '#500'), (1000, '#1000'), (5000, '#5000'), (1000, '#1000')], max_length=30),
        ),
        migrations.AlterField(
            model_name='airtime',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 12, 19, 30, 384625, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='airtime',
            name='network',
            field=models.CharField(choices=[('mtn', 'MTN'), ('glo', 'GLO'), ('airtel', 'AIRTEL'), ('etisalate', 'ETISALAT')], default='MTN', max_length=30),
        ),
        migrations.AlterField(
            model_name='data',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 12, 19, 30, 389625, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='data',
            name='network',
            field=models.CharField(choices=[('mtn', 'MTN'), ('glo', 'GLO'), ('airtel', 'AIRTEL'), ('etisalate', 'ETISALAT')], default='MTN', max_length=30),
        ),
        migrations.AlterField(
            model_name='plan',
            name='network',
            field=models.CharField(choices=[('mtn', 'MTN'), ('glo', 'GLO'), ('airtel', 'AIRTEL'), ('etisalate', 'ETISALAT')], default='MTN', max_length=30),
        ),
        migrations.AlterField(
            model_name='share_and_sell',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 12, 19, 30, 382625, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='share_and_sell',
            name='network',
            field=models.CharField(choices=[('mtn', 'MTN'), ('glo', 'GLO'), ('airtel', 'AIRTEL'), ('etisalate', 'ETISALAT')], default='MTN', max_length=30),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 12, 19, 30, 386625, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Network',
        ),
    ]
