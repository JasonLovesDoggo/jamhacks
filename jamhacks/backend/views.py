from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(
        request,
        "dashboard.html",
        context={
        },
    )


def start(request):
    return render(
        request,
        "start.html",
        context={
            "quests": request.session.get("user.exercises"),
        },
    )


def start_session(request):
    return render(
        request,
        "start_session.html",
        context={
            "quest": "push-ups", # TODO: get quest from request
        },
    )