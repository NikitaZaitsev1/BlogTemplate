from django.urls import path
from user.views import UserView, UserDetailView

urlpatterns = [
    path("", UserView.as_view(), name="account_page"),
    path("self/", UserDetailView.as_view(), name="user_page"),

]
