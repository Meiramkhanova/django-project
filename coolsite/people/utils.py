from .models import *

menu = [{'title': "ABOUT", 'url_name': 'about'},
        {'title': "ARTISTS", 'url_name': 'artists'},
        {'title': "AUDITION", 'url_name': 'addinfo'},
        {'title': "SIGN IN", 'url_name': 'login'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context