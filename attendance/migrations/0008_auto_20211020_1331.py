# Generated by Django 3.2.5 on 2021-10-20 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_mark_attendance1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark_Attendance2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.IntegerField(verbose_name='Roll Number')),
                ('class_name', models.CharField(max_length=20, verbose_name='Class Name')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('time1', models.IntegerField()),
                ('ip_address', models.CharField(max_length=100)),
                ('date1', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=200)),
                ('Master1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roll_no1', to='attendance.master_data')),
            ],
        ),
        migrations.DeleteModel(
            name='Mark_Attendance1',
        ),
    ]
