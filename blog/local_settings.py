DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'HOST': 'localhost',
        'USER': 'danielwolf',
    }
}

TWITTER_API_AUTH = {
    'consumer_key': 'KkWmcUdQLjoZEAFocpK8SaoXa',
    'consumer_secret': 'JB1uqkHqnQgpqTROgIO3e6jsmkBr4lTt4xiMTtG2dUQbFLgPpl',
    'key': '2968681829-Qm4slBXc2GTL6Jif4oQzBtyv8BLEco7HNMYH0Av',
    'secret': 'fJwrQ91wb5qAYH9uBcDAmrj7DVZ6L7uMMQgHZJFJmzeck',
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}