from django.urls import path, include

from librishop.auths.users.views import UserRegisterView

urlpatterns = [
    path('api/', include([
        path('register/', UserRegisterView.as_view(), name='register'),
    ]), name='api'),
]
