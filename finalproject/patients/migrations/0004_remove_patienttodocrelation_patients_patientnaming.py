# Generated by Django 5.2 on 2025-04-14 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_departmentmodel_remove_patienttodocrelation_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patienttodocrelation',
            name='patients',
        ),
        migrations.CreateModel(
            name='PatientNaming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patientmodel')),
            ],
        ),
    ]
