# Generated by Django 5.0.6 on 2024-06-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='password',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]