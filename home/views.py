from django.shortcuts import render

from home.coins import Coins
from home.forms import FeedBackForm
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"


def contacts_view(request):
    form = FeedBackForm()
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                messages.add_message(
                    request, messages.ERROR, "Ваш прошлый запрос еще не обработан")
                messages.add_message(
                    request, messages.ERROR, "Попробуйте позже")
            return redirect(reverse("contacts_page"))
    context = {
        "feedback_form": form,
        "address": "203 Fake St. Mountain View, San Francisco, California, USA",
        "phones": ["+1 232 3235 324", "+00 1122 3344 5566"],
        "emails": ["support@seogram.com", "hello@seogram.com"]
    }
    return render(request, "contacts.html", context)


def coin_price_view(request):
    coins = Coins().get_coins()
    btc_price = coins[0]
    eth_price = coins[1]
    xrp_price = coins[2]
    sol_price = coins[3]
    doge_price = coins[4]
    return render(request, 'coin.html', {'btc_price': btc_price,
                                         'eth_price': eth_price,
                                         'xrp_price': xrp_price,
                                         'sol_price': sol_price,
                                         'doge_price': doge_price})
