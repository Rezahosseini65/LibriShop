from django.urls import path, include

from librishop.auths.users.views import (UserRegisterView, ProfileView,
                                         UserLoginView, ChangePasswordView)

urlpatterns = [
    path('api/', include([
        path('register/', UserRegisterView.as_view(), name='register'),
        path('login/', UserLoginView.as_view(), name='login'),
        path('profile/', ProfileView.as_view(), name='profile'),
        path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    ])),
]
