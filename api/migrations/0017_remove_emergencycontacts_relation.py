# Generated by Django 4.0.3 on 2023-01-21 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_userinfo_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emergencycontacts',
            name='relation',
        ),
    ]
