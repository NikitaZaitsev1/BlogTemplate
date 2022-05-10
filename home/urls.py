from django.urls import path
from home.views import HomeView, AboutView, contacts_view
from django.shortcuts import redirect
from django.urls import reverse


urlpatterns = [
    path("home/", HomeView.as_view(), name="home_page"),
    path("about/", AboutView.as_view(), name="about_page"),
    path("contacts/", contacts_view, name="contacts_page"),
    # path("crypto/", crypto_page, name="crypto_page"),

    path("", lambda request: redirect(reverse("home_page"))),
]