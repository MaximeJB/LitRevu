from django.shortcuts               import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions         import PermissionDenied
from LitRevu.Tickets.models import Tickets
from Tickets.forms                  import TicketForm

@login_required(login_url="/login")
def create_ticket_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("Review:feed")
    else:
        form = TicketForm()
    return render(request, "create_tickets.html", {"form": form})


@login_required(login_url="/login")
def edit_ticket(request, slug):
    ticket = get_object_or_404(Tickets, slug=slug)

    if ticket.user != request.user:
        raise PermissionDenied("Vous ne pouvez éditer que vos propres tickets.")
    
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("Review:ticket", slug=ticket.slug)
    else:
        form = TicketForm(instance=ticket)
    return render(request, "edit_tickets.html", {"form": form})
