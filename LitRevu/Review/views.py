from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from Tickets.models import Tickets
from Tickets.forms import TicketForm
from django.contrib.auth.decorators import login_required
from Review.forms import ReviewForm
from LitRevu.views import homepage
from Comment.forms import CommentForm



def general_feed(request):
    enriched = []
    reviews = Review.objects.all()
    tickets = Tickets.objects.all()
    combined_feed = list(reviews) + list(tickets)

    for item in combined_feed:
        item.type = item.__class__.__name__.lower()
        enriched.append(item)
    return render(request, 'feed.html', {'feed': enriched})

def review_page(request, slug):
    review = Review.objects.get(slug=slug)
    if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.review = review
                comment.save()
                return redirect('Review:review', slug=slug)
    else:
        form = CommentForm()

    comments = review.comments.all()

    return render(request, 'review_page.html', {'review' : review, 'comment_form' :form, 'comments' : comments})

def ticket_page(request, slug):
    ticket = Tickets.objects.get(slug=slug)
    return render(request, 'ticket_page.html', {'ticket' : ticket})

def edit_posts(request, slug):
    try:
        obj = Tickets.objects.get(slug=slug)
        form_try = TicketForm
        template_name = "edit_tickets.html"
        name = "ticket"
    except Tickets.DoesNotExist:
        obj = Review.objects.get(slug=slug)
        form_try = ReviewForm
        template_name = "edit_review.html"
        name = "review"

    if request.method == 'POST':
        form = form_try(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else : 
        form = form_try(instance=obj)

    context = {'form' : form,
               name : obj,
               }
    return render(request, template_name, context)

@login_required(login_url="/login")
def new_post(request):
    return render(request, 'new_post.html')

 
# def comment(request, slug):
#     review = Review.objects.get(slug=slug)
#     if request.method == "POST":
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect(homepage)
#         else : 
#             form = TicketForm()
#         return render(request, "create_tickets.html", {"form" : form })

