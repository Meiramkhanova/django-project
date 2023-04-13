from django.db.models import Count

from .models import *

menu = [{'title': "ABOUT", 'url_name': 'about'},
        {'title': "ARTISTS", 'url_name': 'artists'},
        {'title': "AUDITION", 'url_name': 'addinfo'},
        {'title': "SIGN IN", 'url_name': 'login'}
]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('people'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context