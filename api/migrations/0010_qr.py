# Generated by Django 4.0.3 on 2023-01-20 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_document_remove_address_college_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='qr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='qrcode')),
            ],
        ),
    ]
