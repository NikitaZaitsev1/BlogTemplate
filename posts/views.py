from django.shortcuts import redirect
from django.utils import timezone
from posts.models import Post
from django.shortcuts import render
from posts.forms import PostForm
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'


def post_new_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_page', pk=post.pk)
    else:
        post_form = PostForm()
        return render(request, 'post_new.html', {'post_form': post_form})



# def post_edit_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail_page', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'post_new.html', {'form': form})
