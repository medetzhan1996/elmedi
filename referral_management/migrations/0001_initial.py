# Generated by Django 4.2.4 on 2023-08-14 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directory', '0001_initial'),
        ('contract_management', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_appeal', models.IntegerField(choices=[(1, 'ОМС'), (2, 'ДМС'), (3, 'Платно')])),
                ('place', models.IntegerField(choices=[(1, 'На дому'), (2, 'ПМСП'), (3, 'Амбулаторно'), (4, 'Стационарно')])),
                ('doctor_full_name', models.CharField(blank=True, max_length=180, null=True)),
                ('performing_doctor', models.CharField(blank=True, max_length=180, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('cancel_date', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Не выполнена'), (1, 'Выполнена')], default=0)),
                ('contract_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract_management.contractcustomer')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('directed_hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directed_hospital', to='directory.hospital')),
                ('icd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='directory.icd')),
                ('sending_hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sending_hospital', to='directory.hospital')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referral_services', to='directory.service')),
            ],
        ),
    ]
