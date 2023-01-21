# Generated by Django 4.0.3 on 2023-01-19 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_discussion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=255)),
                ('document_name', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='uploads/')),
                ('encrypted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='address',
            name='college_id',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='class_id',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='college_id',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='teacher_id',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='college_id',
        ),
        migrations.RemoveField(
            model_name='class',
            name='branch_id',
        ),
        migrations.RemoveField(
            model_name='class',
            name='college_id',
        ),
        migrations.RemoveField(
            model_name='communiti',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='discussion',
            name='student_id',
        ),
        migrations.DeleteModel(
            name='Scholarship',
        ),
        migrations.RemoveField(
            model_name='student',
            name='branch_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='college_id',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='college_id',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='branch_id',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='college_id',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='College',
        ),
        migrations.DeleteModel(
            name='Communiti',
        ),
        migrations.DeleteModel(
            name='Discussion',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Suggestion',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
