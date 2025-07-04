# Generated by Django 5.1.4 on 2025-01-31 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='rejection_message',
            field=models.TextField(blank=True, null=True, verbose_name='เหตุผลการไม่อนุมัติ'),
        ),
        migrations.AddField(
            model_name='banner',
            name='status',
            field=models.CharField(choices=[('pending', 'รออนุมัติ'), ('approved', 'อนุมัติแล้ว'), ('rejected', 'ไม่อนุมัติ')], default='pending', max_length=10, verbose_name='สถานะ'),
        ),
    ]
