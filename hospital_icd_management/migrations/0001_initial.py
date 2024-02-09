# Generated by Django 4.2.4 on 2023-08-14 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_icd', to='directory.hospital')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HospitalPackageICD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_at_home_performed', models.BooleanField(default=False)),
                ('social_primary_health_care_performed', models.BooleanField(default=False)),
                ('social_clinical_diagnostic_performed', models.BooleanField(default=False)),
                ('social_hospital_performed', models.BooleanField(default=False)),
                ('vhi_at_home_performed', models.BooleanField(default=False)),
                ('vhi_primary_health_care_performed', models.BooleanField(default=False)),
                ('vhi_clinical_diagnostic_performed', models.BooleanField(default=False)),
                ('vhi_hospital_performed', models.BooleanField(default=False)),
                ('pay_at_home_performed', models.BooleanField(default=False)),
                ('pay_primary_health_care_performed', models.BooleanField(default=False)),
                ('pay_clinical_diagnostic_performed', models.BooleanField(default=False)),
                ('pay_hospital_performed', models.BooleanField(default=False)),
                ('is_perfomed', models.BooleanField(default=False)),
                ('hospital_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_icd_management.hospitalpackage')),
                ('icd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.icd')),
            ],
        ),
    ]