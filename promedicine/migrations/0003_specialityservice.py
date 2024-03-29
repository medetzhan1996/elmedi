# Generated by Django 3.2.4 on 2023-09-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
        ('promedicine', '0002_auto_20230829_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialityService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
                ('services', models.ManyToManyField(to='directory.Service')),
            ],
        ),
    ]
