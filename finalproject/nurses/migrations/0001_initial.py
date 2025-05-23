# Generated by Django 5.2 on 2025-04-14 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NurseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('date_of_birth', models.DateField()),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('qualification', models.CharField(max_length=100)),
                ('years_of_experience', models.IntegerField()),
                ('shift', models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening'), ('Night', 'Night')], max_length=20)),
                ('assigned_room', models.CharField(blank=True, max_length=10, null=True)),
                ('assigned_doctor', models.CharField(blank=True, max_length=100, null=True)),
                ('joined_date', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('departments', models.ForeignKey(blank=True, choices=[('ICU', 'ICU'), ('Pediatrics', 'Pediatrics'), ('Emergency', 'Emergency'), ('OPD', 'OPD')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='nurses.departmentmodel')),
            ],
        ),
    ]
