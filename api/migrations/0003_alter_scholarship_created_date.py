# Generated by Django 4.0.2 on 2022-03-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_college_college_id_alter_college_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
