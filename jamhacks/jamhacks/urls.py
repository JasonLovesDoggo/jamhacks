"""
URL configuration for jamhacks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backend import views
from django.shortcuts import redirect
urlpatterns = [
    path('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix
    path('logout/', views.log_out, name='logout'),
    path('admin/logout/', lambda request: redirect('/logout/', permanent=False)),
    path('admin/', admin.site.urls),
    path("", include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path('socials', views.socials, name='socials'),
    path('results', views.results, name='results'),
    path('quests', views.quests, name='quests'),
    path("start/<int:quest>", views.start, name="start"),
    path("start_session/<int:quest>", views.start_session, name="start_session"),
    ]

