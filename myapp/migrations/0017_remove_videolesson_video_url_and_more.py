# Generated by Django 5.1.4 on 2025-03-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_course_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videolesson',
            name='video_url',
        ),
        migrations.AddField(
            model_name='videolesson',
            name='google_drive_id',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Google Drive File ID'),
        ),
    ]
