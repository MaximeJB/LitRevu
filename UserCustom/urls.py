from django.urls import path
from . import views

app_name = "UserCustom"

urlpatterns = [
    path("register", views.register_view, name="user-register"),
    path("login/", views.login_view, name="user-login"),
    path("logout", views.logout_view, name="user-logout"),
]
