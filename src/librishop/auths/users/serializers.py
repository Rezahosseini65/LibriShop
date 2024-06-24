from rest_framework import serializers

from .models import Profile, CustomUser


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source='user.firstname')
    lastname = serializers.CharField(source='user.lastname')

    class Meta:
        model = Profile
        fields = ('id', 'firstname', 'lastname', 'phone_number',
                  'province', 'city', 'address', 'postal_code')
