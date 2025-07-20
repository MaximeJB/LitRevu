from django.forms import ModelForm
from Tickets.models import Tickets

class TicketForm(ModelForm):
    class Meta : 
        model = Tickets
        fields = ["title", "description", "user", "image"]