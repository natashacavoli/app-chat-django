"""."""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate


def index(request):
    """."""
    return render(request, "index.html")


def login(request):
    """."""
    return render(request, "login.html")


def define_login(request, user):
    """."""
    request.session["id"] = user.id
    request.session["name"] = user.name


def process_login(request):
    """."""
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)

    if user:
        define_login(request, user)

        return HttpResponseRedirect("/me")

    return HttpResponse("sorry")


def logout(request):
    """."""
    try:
        del request.session["id"]
    except:
        pass

    return HttpResponseRedirect("/login")
