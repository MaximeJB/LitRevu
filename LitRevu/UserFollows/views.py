from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import UserFollows
from Tickets.models import Tickets
from Review.models import Review
from Comment.models import Comment
from UserCustom.models import UserApp
from .forms import FollowForm


User = get_user_model()


@login_required(login_url="/login")
def follow_user(request, username):
    follow_target = get_object_or_404(User, username=username)
    if request.user != follow_target:
        if not request.user.following.filter(id=follow_target.id).exists():
            UserFollows.objects.create(user=request.user, followed_user=follow_target)
            messages.success(request, f"Vous suivez maintenant {follow_target.username}.")
        return redirect("UserFollow:profil", username=username)
    else:
        redirect("Review:feed")


@login_required(login_url="/login")
def unfollow_user(request, username):
    unfollow_target = get_object_or_404(User, username=username)
    UserFollows.objects.filter(
        user=request.user, followed_user=unfollow_target
    ).delete()
    return redirect("UserFollow:profil", username=username)


@login_required(login_url="/login")
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)

    reviews_qs = Review.objects.filter(user=profile_user)
    tickets_qs = Tickets.objects.filter(user=profile_user)
    reviews_count = reviews_qs.count()
    tickets_count = tickets_qs.count()
    latest_comments = Comment.objects.filter(user=profile_user).order_by(
        "-time_created"
    )[:2]
    following = profile_user.following.select_related("followed_user").all()
    followers = profile_user.followed_by.select_related("user").all()
    is_following = (
        request.user.is_authenticated
        and request.user.following.filter(followed_user=profile_user).exists()
    )
    is_blocked = profile_user in request.user.blocked_user.all()

    return  render(
        request,
        "users/profile_page.html",
        {
            "profile_user": profile_user,
            "reviews_count": reviews_count,
            "tickets_count": tickets_count,
            "latest_comments": latest_comments,
            "is following": is_following,
            "following": following,
            "followers": followers,
            "search_form": FollowForm(),
            "is_following": is_following,
            "is_blocked": is_blocked,
        },
    )


@login_required
def block_user(request, username):
    if request.method == "POST":
        target = get_object_or_404(User, username=username)
        if target != request.user:
            request.user.blocked_user.add(target)
    unfollow_user(request, username)
    return redirect("Review:feed")


@login_required
def unblock_user(request, username):
    if request.method == "POST":
        target = get_object_or_404(User, username=username)
        if target in request.user.blocked_user.all():
            request.user.blocked_user.remove(target)
    return redirect("Review:feed")


@login_required
def search_user(request):
    username = request.POST.get("username")

    try:
        follow_target = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.error(request, f"L'utilisateur '{username}' n'existe pas.")
        return redirect("UserFollow:profil", username=request.user.username)
    return redirect("UserFollow:profil", username=follow_target.username)


@login_required(login_url="/login")
def my_profile_redirect(request):
    return redirect("UserFollow:profil", username=request.user.username)
