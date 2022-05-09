from django.shortcuts import render
from home.forms import FeedBackForm
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


def home_view(request):
    return render(request, "home.html", {})


def about_view(request):
    return render(request, "about.html", {})


def contacts_view(request):
    form = FeedBackForm()
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                messages.add_message(request, messages.ERROR, "Ваш прошлый запрос еще не обработан")
                messages.add_message(request, messages.ERROR, "Попробуйте позже")
            return redirect(reverse("contacts_page"))
    context = {
        "feedback_form": form,
        "address": "203 Fake St. Mountain View, San Francisco, California, USA",
        "phones": ["+1 232 3235 324", "+00 1122 3344 5566"],
        "emails": ["support@seogram.com", "hello@seogram.com"]
    }
    return render(request, "contacts.html", context)
