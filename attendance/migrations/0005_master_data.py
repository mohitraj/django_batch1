# Generated by Django 3.2.5 on 2021-10-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_rename_attedance_att'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.IntegerField(verbose_name='Roll Number')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('class_name', models.CharField(max_length=20, verbose_name='Class Name')),
            ],
            options={
                'unique_together': {('roll_number', 'class_name')},
            },
        ),
    ]
