import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode


oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("dashboard")))


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("dashboard")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )


def dashboard(request):
    return render(
        request,
        "dashboard.html",
        context={
            "pretty": json.dumps(request.session.get("user"), indent=4),
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
