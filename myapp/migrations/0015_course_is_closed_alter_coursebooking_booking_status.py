# Generated by Django 5.1.4 on 2025-02-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_coursedetails_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='coursebooking',
            name='booking_status',
            field=models.CharField(choices=[('pending', 'รอการยืนยัน'), ('confirmed', 'จองสำเร็จ'), ('canceled', 'จองไม่สำเร็จ')], default='pending', max_length=20),
        ),
    ]
