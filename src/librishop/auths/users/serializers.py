from django.core.validators import MinLengthValidator

from rest_framework import serializers

from .models import Profile, CustomUser
from .validators import number_validator, letter_validator


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True, required=True, validators=[
        number_validator,
        letter_validator,
        MinLengthValidator(limit_value=8),
    ])

    confirm_password = serializers.CharField(write_only=True, validators=[
        MinLengthValidator(limit_value=8)
    ])

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'confirm_password']

    def validate_email(self, email):
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("email Already Taken")
        return email

    def validate(self, data):
        if not data.get("password") or not data.get("confirm_password"):
            raise serializers.ValidationError("Please fill password and confirm password")

        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError("confirm password is not equal to password")
        return data

    def create(self, validated_data):
        """
        Override the create method to handle user creation with password hashing.
        """
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = CustomUser.objects.create_user(email=email, password=password)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'firstname', 'lastname', 'phone_number',
            'province', 'city', 'address', 'postal_code'
        ]
