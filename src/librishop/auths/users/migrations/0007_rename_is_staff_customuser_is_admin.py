# Generated by Django 5.0.6 on 2024-06-24 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_customuser_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]