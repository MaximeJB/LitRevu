from django.shortcuts                   import render, redirect, get_object_or_404
from Tickets.models                     import Tickets
from Review.models                      import Review
from Tickets.forms                      import TicketForm
from django.contrib.auth.decorators     import login_required
from django.contrib.auth                import get_user_model
from Review.forms                       import ReviewForm
from Comment.forms                      import CommentForm
from django.core.exceptions             import PermissionDenied
from django.contrib                     import messages

User = get_user_model()


@login_required(login_url="/login")
def general_feed(request):
    enriched = []

    followed_ids = list(
        request.user.following.values_list("followed_user__id", flat=True)
    )

    followed_ids.append(request.user.id)

    blocked = request.user.blocked_user.all()
    blocked_by = request.user.Blocked_by.all()

    reviews = (
        Review.objects.filter(user__id__in=followed_ids)
        .exclude(user__in=blocked)
        .exclude(user__in=blocked_by)
    )
    tickets = (
        Tickets.objects.filter(user__id__in=followed_ids)
        .exclude(user__in=blocked)
        .exclude(user__in=blocked_by)
    )

    combined_feed = list(reviews) + list(tickets)
    for item in combined_feed:
        item.type = item.__class__.__name__.lower()
        enriched.append(item)
    enriched.sort(key=lambda x: x.time_created, reverse=True)
    return render(request, "feed.html", {"feed": enriched})


@login_required(login_url="/login")
def review_page(request, slug):
    review = get_object_or_404(Review, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return redirect("Review:review", slug=slug)
    else:
        form = CommentForm()

    comments = review.comments.all().order_by("-time_created")

    return render(
        request,
        "review_page.html",
        {"review": review, "comment_form": form, "comments": comments})


@login_required(login_url="/login")
def ticket_page(request, slug):
    ticket = get_object_or_404(Tickets, slug=slug)
    return render(request, "ticket_page.html", {"ticket": ticket})


@login_required(login_url="/login")
def edit_posts(request, slug):

    try:
        obj = get_object_or_404(Tickets,slug=slug)
        form_try = TicketForm
        template_name = "edit_tickets.html"
        name = "ticket"
        redirect_url = "Review:ticket"
    except Tickets.DoesNotExist:
        obj = get_object_or_404(Review, slug=slug)
        form_try = ReviewForm
        template_name = "edit_review.html"
        name = "review"
        redirect_url = "Review:review"

    if obj.user != request.user:
        raise PermissionDenied("Seul l'auteur peut modifier ce post.")

    if request.method == "POST":
        form = form_try(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(redirect_url, slug=obj.slug)
    else:
        form = form_try(instance=obj)

    context = {
        "form": form,
        name: obj,
    }
    return render(request, template_name, context)

@login_required(login_url="/login")
def delete_post(request, slug):
    """Vue pour supprimer un ticket ou une review"""
    try:
        obj = Tickets.objects.get(slug=slug)
        post_type = "ticket"
    except Tickets.DoesNotExist:
        try:
            obj = Review.objects.get(slug=slug)
            post_type = "review"
        except Review.DoesNotExist:
            messages.error(request, "Ce post n'existe pas.")
            return redirect("Review:feed")

    
    if obj.user != request.user:
        raise PermissionDenied("Seul l'auteur peut supprimer ce post.")

    if request.method == "POST":
        obj.delete()
        messages.success(request, f"Votre {post_type} a été supprimé avec succès.")
        return redirect("Review:feed")
    
    
    return render(request, "confirm_delete.html", {
        "object": obj,
        "post_type": post_type
    })

@login_required(login_url="/login")
def create_review_view(request, ticket_id=None):
    ticket = None
    ticket_id = request.POST.get("ticket_id") or request.GET.get("ticket_id")
    if ticket_id:
        ticket = get_object_or_404(Tickets, id=ticket_id)

    if request.method == "POST":
        ticket_form = None if ticket else TicketForm(request.POST, request.FILES)
        form = ReviewForm(request.POST)

        if form.is_valid() and (ticket or ticket_form.is_valid()):
            if not ticket:
                ticket = ticket_form.save(commit=False)
                ticket.user = request.user
                ticket.save()

            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("Review:feed")
    else:
        ticket_form = None if ticket else TicketForm()
        form = ReviewForm()
    return render(
        request,
        "create_review.html",
        {"ticket": ticket, "ticket_form": ticket_form, "form": form},
    )


@login_required(login_url="/login")
def my_posts(request, username):
    if username != request.user.username:
        return redirect("Review:my-posts", request.user.username)

    user = request.user
    user_reviews = Review.objects.filter(user=user)
    user_tickets = Tickets.objects.filter(user=user)

    enriched = []
    combined = list(user_reviews) + list(user_tickets)
    for item in combined:
        item.type = item.__class__.__name__.lower()
        enriched.append(item)
    enriched.sort(key=lambda x: x.time_created, reverse=True)

    return render(
        request,
        "my_posts.html",
        {
            "posts": enriched,
            "username": user.username,
        },
    )


def comment(request, slug):
    review = get_object_or_404(Review, slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect("Review:review", slug=review.slug)
    else:
        form = CommentForm()
    return render(
        request, "comments/create_comment.html", {"form": form, "review": review}
    )
