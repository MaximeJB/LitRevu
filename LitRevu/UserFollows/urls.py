from django.urls import path
from . import views

app_name = 'UserFollow'

urlpatterns = [ 
    path('<slug:username>/', views.profile_view, name = 'profil'),
    path('<slug:username>/follow/', views.follow_user, name = 'follow-user'),
    path('<slug:username>/unfollow/', views.unfollow_user, name = 'unfollow-user'),
]