from django.urls import path
from posts.views import post_list_view, post_detail_view, post_new_view, post_edit_view

urlpatterns = [
    path('post/', post_list_view, name='post_list_page'),
    path('post/<int:pk>/', post_detail_view, name='post_detail_page'),
    path('post/new/', post_new_view, name='post_new_page'),
    path('post/<int:pk>/edit/', post_edit_view, name='post_edit_page'),
]
