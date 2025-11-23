from django.urls import path
from . import views

app_name = "Tickets"

urlpatterns = [
    path("create-ticket", views.create_ticket_view, name="create-ticket"),
    path("edit", views.edit_ticket, name="edit-ticket"),
]
