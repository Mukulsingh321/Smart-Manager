# Generated by Django 4.0.5 on 2022-06-27 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_app', '0019_alter_login_emp_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_emp',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]