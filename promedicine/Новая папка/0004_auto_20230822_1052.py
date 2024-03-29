# Generated by Django 3.2 on 2023-08-22 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
        ('promedicine', '0003_alter_professionalexamination_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hazardserviсe',
            name='hazard',
        ),
        migrations.RemoveField(
            model_name='hazardserviсe',
            name='service',
        ),
        migrations.RemoveField(
            model_name='professionhazard',
            name='hazard',
        ),
        migrations.RemoveField(
            model_name='professionhazard',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='professionalexamination',
            name='factory',
        ),
        migrations.RemoveField(
            model_name='professionalexamination',
            name='profession',
        ),
        migrations.AddField(
            model_name='professionalexamination',
            name='insurer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='directory.insurer'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Factory',
        ),
        migrations.DeleteModel(
            name='Hazard',
        ),
        migrations.DeleteModel(
            name='HazardServiсe',
        ),
        migrations.DeleteModel(
            name='Profession',
        ),
        migrations.DeleteModel(
            name='ProfessionHazard',
        ),
    ]
