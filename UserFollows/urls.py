from django.urls import path
from . import views

app_name = "UserFollow"

urlpatterns = [
    path("<slug:username>/profile-page/", views.profile_view, name="profil"),
    path("profile-page/", views.my_profile_redirect, name="my-profil"),
    path("<slug:username>/follow/", views.follow_user, name="follow-user"),
    path("<slug:username>/unfollow/", views.unfollow_user, name="unfollow-user"),
    path("<slug:username>/block/", views.block_user, name="block-user"),
    path("<slug:username>/unblock/", views.unblock_user, name="unblock-user"),
    path("search-user/", views.search_user, name="search-user"),
]
