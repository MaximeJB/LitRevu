from django.urls import path
from . import views

app_name = "Review"

urlpatterns = [
    path("feed", views.general_feed, name="feed"),
    path("new-review/", views.create_review_view, name="create-review"),
    path("ticket/<slug:slug>", views.ticket_page, name="ticket"),
    path("review/<slug:slug>", views.review_page, name="review"),
    path("edit/<slug:slug>", views.edit_posts, name="edit_posts"),
    path("<slug:username>/posts", views.my_posts, name="my-posts"),
    path("tickets/<int:ticket_id>/review/",views.create_review_view,name="ticket-review",),
]
