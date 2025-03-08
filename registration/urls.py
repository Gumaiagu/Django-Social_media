from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/singup", views.SignUpView.as_view(), name="singup"),
    path('users/<str:who>', views.user_profile),
    path('ban_user/<str:banned_user_id>', views.ban_user, name="banuser"),
    path('unban_user/<str:banned_user_id>', views.unban_user, name="unbanuser"),
]
