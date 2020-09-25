"""."""
from django.shortcuts import render
from utils.decorators import login_required

from .models import Users, Friends


@login_required
def index(request):
    """."""
    id = request.session["id"]

    res = Users.objects.get(id=id)

    data = {"me": res}

    request.session["uid"] = res.uid.hex

    return render(request, "user.html", data)


@login_required
def about(request):
    """."""
    id = request.session["id"]

    res = Users.objects.get(id=id)

    data = {"me": res}

    request.session["uid"] = res.uid.hex

    return render(request, "me.html", data)


@login_required
def friends(request):
    """."""
    id = request.session["id"]

    res = Friends.objects.filter(user_id=id)

    for i in res:

        i.chat_id = i.chat_id.hex if i.chat_id else ""

    data = {"friends": res}

    return render(request, "friends.html", data)
