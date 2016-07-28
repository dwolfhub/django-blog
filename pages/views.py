from django.shortcuts import get_object_or_404, render
from django.core.cache import cache

from django.conf import settings
from posts.models import Post
from .models import Page
import oauth2
from datetime import datetime
import json


def home(request):
    page = get_object_or_404(Page, slug='home')
    posts = Post.objects.order_by('-published')[:5]

    tweets = cache.get('tweets')
    if not tweets:
        tweets = get_tweets()
        cache.set('tweets', tweets)

    return render(request, 'pages/home.html', {'page': page, 'posts': posts, 'tweets': tweets,})


def about(request):
    page = get_object_or_404(Page, slug='about')

    return render(request, 'pages/about.html', {'page': page,})


def get_tweets():
    tweets = []

    consumer = oauth2.Consumer(
        key=settings.TWITTER_API_AUTH['consumer_key'],
        secret=settings.TWITTER_API_AUTH['consumer_secret']
    )
    token = oauth2.Token(key=settings.TWITTER_API_AUTH['key'], secret=settings.TWITTER_API_AUTH['secret'])
    client = oauth2.Client(consumer, token)
    resp, content = client.request('https://api.twitter.com/1.1/statuses/user_timeline.json?count=5')

    if content:
        content = json.loads(content)
        for tweet in content:
            # Take out parts of the datetime string that are tough to parse
            date_parts = tweet['created_at'].split(' ')
            date_string = '{} {} {} {}'.format(date_parts[1], date_parts[2], date_parts[3], date_parts[5])
            date_obj = datetime.strptime(date_string, '%b %d %H:%M:%S %Y')
            tweets.append({
                'created': date_obj,
                'text': tweet['text'],
                'url': 'https://twitter.com/statuses/{}'.format(tweet['id_str']),
                'username': tweet['user']['screen_name'],
            })

    return tweets
