from django.urls import path, include

from librishop.auths.users.views import UserRegisterView, ProfileView, UserLoginView

urlpatterns = [
    path('api/', include([
        path('register/', UserRegisterView.as_view(), name='register'),
        path('login/', UserLoginView.as_view(), name='login'),
        path('profile/', ProfileView.as_view(), name='profile'),
    ])),
]
