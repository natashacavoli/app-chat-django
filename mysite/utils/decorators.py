"""."""
from django.http import HttpResponse

from user.models import Friends


def login_required(function):
    """."""
    def wrapper(request, **kwargs):
        """."""
        if request.session.get("id"):
            return function(request, **kwargs)

        else:
            return HttpResponse("please authenticate")

    return wrapper


def is_friend(function):
    """."""
    def wrapper(request, **kwargs):
        """."""
        if kwargs.get("room"):

            r = Friends.objects.filter(user_id=request.session["id"])

            friends = [i.chat_id.hex for i in r if i.chat_id]

            if kwargs["room"] not in friends:

                return HttpResponse("not your friend :@")

            return function(request, **kwargs)

        else:
            return HttpResponse("invalid param")

    return wrapper
