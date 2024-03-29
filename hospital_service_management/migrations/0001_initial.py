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
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', to='directory.hospital')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HospitalPackageService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_at_home', models.FloatField(blank=True, null=True)),
                ('state_primary_health_care', models.FloatField(blank=True, null=True)),
                ('state_clinical_diagnostic', models.FloatField(blank=True, null=True)),
                ('state_hospital', models.FloatField(blank=True, null=True)),
                ('vhi_at_home_coefficient', models.FloatField(blank=True, null=True)),
                ('vhi_primary_health_care_coefficient', models.FloatField(blank=True, null=True)),
                ('vhi_clinical_diagnostic_coefficient', models.FloatField(blank=True, null=True)),
                ('vhi_hospital_coefficient', models.FloatField(blank=True, null=True)),
                ('vhi_price', models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True)),
                ('pay_at_home_coefficient', models.FloatField(blank=True, null=True)),
                ('pay_primary_health_care_coefficient', models.FloatField(blank=True, null=True)),
                ('pay_clinical_diagnostic_coefficient', models.FloatField(blank=True, null=True)),
                ('pay_hospital_coefficient', models.FloatField(blank=True, null=True)),
                ('pay_base_price', models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True)),
                ('is_checked', models.BooleanField(default=False)),
                ('hospital_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_service_management.hospitalpackage')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', to='directory.service')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
