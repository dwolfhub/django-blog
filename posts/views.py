from django.shortcuts import render, get_object_or_404
from posts.models import Post


def single(request, slug=''):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'posts/post.html', {'post': post})
