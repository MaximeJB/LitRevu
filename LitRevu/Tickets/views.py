from django.shortcuts import render, redirect
from Tickets.forms import TicketForm
from LitRevu.views import homepage

def create_ticket_view(request):
      if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(homepage)
      else : 
          form = TicketForm()
      return render(request, "create_tickets.html", {"form" : form })

def edit_ticket(request, slug):
    ticket = TicketForm.objects.get(slug=slug)
    form = TicketForm(instance=ticket)
    return render(request, "edit_tickets.html", {"form" : form})




    ##TODO : 
## CreateTicketView pour ajouter un billet en version user
## URL : /tickets/create
## UpdateView pour modifier ticket
#faire liste de tickets avant, pour pouvoir afficher la liste, cliquer arriver sur la page, du ticket, et edit 
## URL : /tickets/edit
## DeleteTicketView
## Confirmation pop up
## URL : /tickets/delete ou retour homepage
## Même chose avec Review regarder cahier des charges