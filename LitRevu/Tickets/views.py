from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Tickets.forms import TicketForm

@login_required(login_url="/login")
def create_ticket_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            form.save()
            return redirect("Review:feed")
    else:
        form = TicketForm()
    return render(request, "create_tickets.html", {"form": form})


@login_required(login_url="/login")
def edit_ticket(request, slug):
    ticket = TicketForm.objects.get(slug=slug)
    form = TicketForm(instance=ticket)
    return render(request, "edit_tickets.html", {"form": form})
