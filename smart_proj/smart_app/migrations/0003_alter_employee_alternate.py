# Generated by Django 4.0.4 on 2022-06-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_app', '0002_login_emp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='alternate',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]