# Generated by Django 4.0.4 on 2022-06-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_app', '0005_remove_emp_role_role_id_emp_role_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_emp',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
