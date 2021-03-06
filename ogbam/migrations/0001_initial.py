# Generated by Django 2.1.1 on 2018-09-27 09:04

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('BankName', models.CharField(blank=True, choices=[('first bank', 'First Bank of Nigeria'), ('uba', 'UBA'), ('access', 'Access Bank'), ('wema', 'Wema Bank'), ('diamond', 'Diamond Bank'), ('heritage', 'Heritage bank'), ('sky', 'Sky Bank'), ('stanbic', 'Stanbic IBTC'), ('sterling', 'Sterling Bank'), ('union', 'Union Bank'), ('zenith', 'Zenith Bank'), ('unity', 'Unity Bank'), ('fcmb', 'FCMBank'), ('gtb', 'GTBank'), ('fidelity', 'FIdelity Bank'), ('eco', 'ECO Bank')], max_length=100)),
                ('AccountNumber', models.CharField(blank=True, max_length=30)),
                ('Phone', models.CharField(blank=True, max_length=30)),
                ('AccountName', models.CharField(blank=True, max_length=30)),
                ('Balance', models.FloatField(default=0.0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Airtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(blank=True, max_length=30)),
                ('mobile_number', models.CharField(blank=True, max_length=30)),
                ('amount', models.CharField(blank=True, max_length=30)),
                ('Status', models.CharField(choices=[('pending', 'Pending'), ('failed', 'Failed'), ('successful', 'Successful')], default='Pending', max_length=30)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2018, 9, 27, 9, 4, 59, 417, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(choices=[('mtn_1gb', 'MTN  1GB  #800'), ('mtn_2gb', 'MTN  2GB  #1,550'), ('mtn_3gb', 'MTN  3GB  #2,250'), ('mtn_5gb', 'MTN  5GB  #3,750'), ('9mobile_1gb', '9MOBILE  1GB  #700'), ('9mobile_1.5gb', '9MOBILE  1.5GB  #1,050'), ('9mobile_2gb', '9MOBILE  2GB  #1,400'), ('9mobile_3gb', '9MOBILE  3GB  #2,000'), ('9mobile_5gb', '9MOBILE  5GB  #3,500'), ('9mobile_11gb', '9MOBILE 11GB  #7,500'), ('airtel_1.5gb', 'AIRTEL 1.5GB #900'), ('airtel_3.5gb', 'AIRTEL 3.5GB #1,0850'), ('airtel_5gb', 'AIRTEL 5GB #2,330'), ('airtel_7gb', 'AIRTEL 7GB #3,300'), ('glo_1.6gb', 'GLO 1.6/2GB 900#'), ('glo_3.65gb', 'GLO 3333.65/4.5GB  2,250#'), ('glo_5.7gb', 'GLO 5.7/7.2GB #2,650'), ('glo_10gb', 'GLO 10/12.5GB #3,550'), ('glo_20gb', 'GLO 20GB #7,000'), ('glo_26gb', 'GLO 26GB #8000'), ('glo_42gb', 'GLO 42GB #13,000')], max_length=50, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=30)),
                ('method', models.CharField(blank=True, choices=[('Airtime Pin', 'Airtime Pin'), ('Bank  Transfer', 'Bank Transfer'), ('Wallet', 'Wallet'), ('Airtime tranfer', 'Airtime tranfer')], max_length=30)),
                ('Status', models.CharField(choices=[('pending', 'Pending'), ('failed', 'Failed'), ('successful', 'Successful')], default='Pending', max_length=30)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2018, 9, 27, 9, 4, 59, 16041, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Network', models.CharField(blank=True, max_length=30)),
                ('About', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_data', models.CharField(blank=True, max_length=30)),
                ('plan_amount', models.CharField(blank=True, max_length=30)),
                ('month_validate', models.CharField(blank=True, max_length=30)),
                ('network', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ogbam.Network')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Share_And_Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(blank=True, max_length=30)),
                ('amount', models.CharField(blank=True, max_length=30)),
                ('Status', models.CharField(choices=[('pending', 'Pending'), ('failed', 'Failed'), ('successful', 'Successful')], default='Pending', max_length=30)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2018, 9, 27, 9, 4, 59, 417, tzinfo=utc))),
                ('network', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ogbam.Network')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='withdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumber', models.CharField(blank=True, max_length=30)),
                ('accountName', models.CharField(blank=True, max_length=30)),
                ('bankName', models.CharField(blank=True, choices=[('first bank', 'First Bank of Nigeria'), ('uba', 'UBA'), ('access', 'Access Bank'), ('wema', 'Wema Bank'), ('diamond', 'Diamond Bank'), ('heritage', 'Heritage bank'), ('sky', 'Sky Bank'), ('stanbic', 'Stanbic IBTC'), ('sterling', 'Sterling Bank'), ('union', 'Union Bank'), ('zenith', 'Zenith Bank'), ('unity', 'Unity Bank'), ('fcmb', 'FCMBank'), ('gtb', 'GTBank'), ('fidelity', 'FIdelity Bank'), ('eco', 'ECO Bank')], max_length=100)),
                ('amount', models.CharField(blank=True, max_length=30)),
                ('Status', models.CharField(choices=[('pending', 'Pending'), ('failed', 'Failed'), ('successful', 'Successful')], default='Pending', max_length=30)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2018, 9, 27, 9, 4, 59, 16041, tzinfo=utc))),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='network',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ogbam.Network'),
        ),
        migrations.AddField(
            model_name='data',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='airtime',
            name='network',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ogbam.Network'),
        ),
        migrations.AddField(
            model_name='airtime',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
