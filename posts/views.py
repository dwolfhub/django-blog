from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from posts.models import Post


def single(request, slug=''):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'posts/post.html', {'post': post})


def author(request, username=''):
    page = request.GET.get('page')

    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    paginator = Paginator(posts, 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'posts/author.html', {'posts': posts, 'author': user,})
