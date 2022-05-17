from django.urls import path
from posts.views import PostListView, PostDetailView
from posts.views import post_new_view

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail_page'),
    path('post/new/', post_new_view, name='post_new_page'),

]
