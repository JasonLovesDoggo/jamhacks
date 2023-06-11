from django.shortcuts import render
from django.contrib.auth import logout

from .models import CoreUser, Quest, Badge


# Create your views here.

def dashboard(request):
    return render(
        request,
        "dashboard.html",
        context={
            "quests": Quest.objects.all(),
        },
    )


def quests(request):
    return render(
        request,
        "quests.html",
        context={
        },
    )


def start(request, quest):
    return render(
        request,
        "start.html",
        context={
            "quest": Quest.objects.get(pk=quest),
        },
    )


def start_session(request, quest):
    return render(
        request,
        "start_session.html",
        context={
            "quest": "push-ups",  # TODO: get quest from request
        },
    )


# display profile
def profile(request):
    return render(
        request,
        "profile.html",
        context={
            
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