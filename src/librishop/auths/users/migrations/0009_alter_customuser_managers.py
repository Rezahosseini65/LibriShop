# Generated by Django 5.0.6 on 2024-06-25 07:53

import librishop.auths.users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_is_admin_customuser_is_staff'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', librishop.auths.users.models.CustomUserManager()),
            ],
        ),
    ]