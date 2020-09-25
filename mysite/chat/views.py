"""."""
from django.shortcuts import render
from utils.decorators import login_required, is_friend


@login_required
def index(request):
    """."""
    return render(request, "chat/index.html")


@login_required
@is_friend
def room(request, room):
    """."""
    return render(request, "chat/room.html", {
        "room": room,
        "name": request.session["name"]})
