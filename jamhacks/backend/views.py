from django.shortcuts import render
from django.contrib.auth import logout

from .models import CoreUser, Quest, Badge
import json


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


def socials(request):
    return render(
        request,
        "socials.html",
        context={
            'users': CoreUser.objects.all(),
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
    # request.session['exercise'] = json.dumps(Quest.objects.get(pk=quest).exercises.first())
    # print(request.session['exercise'])
    return render(
        request,
        "start_session.html",
        context={
            'exercise': Quest.objects.get(pk=quest).exercises.first(),
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


# display results
def results(request):
    return render(
        request,
        "results.html",
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

from django.shortcuts import redirect
def log_out(request):
    logout(request)
    return render(
        request,
        "registration/logout.html",
    )