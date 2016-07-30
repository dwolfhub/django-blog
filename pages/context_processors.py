from .models import Page


def pages_processor(request):
    pages = Page.objects.all().exclude(slug='home').order_by('title')
    print pages

    return {'pages': pages}
