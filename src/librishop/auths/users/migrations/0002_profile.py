# Generated by Django 5.0.6 on 2024-06-23 13:49

import django.db.models.deletion
import librishop.auths.users.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, validators=[librishop.auths.users.validators.PhoneNumberValidator()])),
                ('province', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
                ('address', models.CharField(blank=True, max_length=1024, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, validators=[librishop.auths.users.validators.PostalCodeValidator()])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'indexes': [models.Index(fields=['province'], name='users_profi_provinc_f9b7a8_idx'), models.Index(fields=['city'], name='users_profi_city_2fdd0b_idx')],
            },
        ),
    ]
