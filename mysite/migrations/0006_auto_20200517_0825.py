# Generated by Django 2.2.10 on 2020-05-17 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20200516_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activityperiod',
            old_name='id1',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id1',
            new_name='user_id',
        ),
    ]
