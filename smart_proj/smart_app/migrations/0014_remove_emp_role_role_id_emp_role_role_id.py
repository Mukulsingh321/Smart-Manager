# Generated by Django 4.0.4 on 2022-06-13 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_app', '0013_remove_emp_role_role_id_emp_role_role_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp_role',
            name='role_id',
        ),
        migrations.AddField(
            model_name='emp_role',
            name='role_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smart_app.role_master'),
        ),
    ]