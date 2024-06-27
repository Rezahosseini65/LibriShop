from django.contrib.auth import update_session_auth_hash

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Profile, CustomUser
from .serializers import (CustomUserRegisterSerializer, ProfileSerializer,
                          CustomUserLoginSerializer, ChangePasswordSerializer)


class UserRegisterView(generics.CreateAPIView):
    serializer_class = CustomUserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(generics.GenericAPIView):
    serializer_class = CustomUserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        }, status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        """Return the current authenticated user."""
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check old password
        if not self.object.check_password(serializer.validated_data.get("password")):
            return Response({"password": ["Wrong password"]}, status=status.HTTP_400_BAD_REQUEST)

        # Set new password
        new_password = serializer.validated_data.get("new_password")
        self.object.set_password(new_password)
        self.object.save()

        # Update the session hash to keep the user logged in
        update_session_auth_hash(request, self.object)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
