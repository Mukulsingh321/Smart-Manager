# Generated by Django 4.0.4 on 2022-06-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_app', '0006_alter_login_emp_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp_role',
            name='role_id',
        ),
        migrations.AddField(
            model_name='emp_role',
            name='role_id',
            field=models.ManyToManyField(to='smart_app.role_master'),
        ),
    ]