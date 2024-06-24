from django.urls import path, include

from rest_framework.authtoken import views

from librishop.auths.users.views import UserRegisterView, ProfileView

urlpatterns = [
    path('api/', include([
        path('register/', UserRegisterView.as_view(), name='register'),
        path('login/', views.obtain_auth_token, name='login'),
        path('profile/', ProfileView.as_view(), name='profile'),
    ])),
]
