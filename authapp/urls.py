from django.contrib.auth import views
from django.urls import path
from .views import *
from .forms import LoginForm

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/", ChangePView.as_view(), name="password_change"
    ),
    path("password_reset/", ResetPasswordView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(template_name='registration/passwordresetdone.html'),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordSetView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(template_name='registration/passwordresetcomplete.html'),
        name="password_reset_complete",
    ),
    path('register/', registerview, name='register'),
    path('dashboard/', dashboardview, name='dashboard'),
    path('', dashboardview, name='dashboard1'),
]
