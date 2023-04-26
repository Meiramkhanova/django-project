from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [{'title': "ABOUT", 'url_name': 'about'},
        {'title': "AUDITION", 'url_name': 'addinfo'},
        {'title': "FEEDBACK", 'url_name': 'contact'},
]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats  = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('people'))
            cache.set('cats', cats, 60)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context