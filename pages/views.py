from django.shortcuts import get_object_or_404, render

from posts.models import Post
from .models import Page


def home(request):
    page = get_object_or_404(Page, slug='home')
    posts = Post.objects.order_by('-published')[:5]

    return render(request, 'pages/home.html', {'page': page, 'posts': posts})
