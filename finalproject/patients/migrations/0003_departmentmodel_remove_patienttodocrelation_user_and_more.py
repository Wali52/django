# Generated by Django 5.2 on 2025-04-14 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('patients', '0002_patienttodocrelation'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='patienttodocrelation',
            name='user',
        ),
        migrations.AddField(
            model_name='patienttodocrelation',
            name='patients',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.patientmodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patienttodocrelation',
            name='doctor',
            field=models.ManyToManyField(related_name='patient', to='doctor.doctormodel'),
        ),
    ]
