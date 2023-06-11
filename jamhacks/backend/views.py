from django.shortcuts import render
from django.contrib.auth import logout

from .models import CoreUser, Quest


# Create your views here.

def dashboard(request):
    return render(
        request,
        "dashboard.html",
        context={
            "quests": Quest.objects.all(),
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
            "quest": "push-ups",  # TODO: get quest from request
        },
    )


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class CoreUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CoreUser


class SignUpView(generic.CreateView):
    form_class = CoreUserCreationForm

    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def log_out(request):
    logout(request)
    return render(
        request,
        "registration/logout.html",
    )