from django.db.models import Count

from .models import *

menu = [{'title': "Главная страница", 'url_name': ''},
        {'title': "Обо мне", 'url_name': 'about'},
        {'title': "Мои проекты", 'url_name': 'projects'},
        {'title': "Контакты", 'url_name': 'contacts'},
        {'title': "Отзывы", 'url_name': 'reviews'},
        {'title': "Добавление отзыва", 'url_name': 'add_review'},
]

class DataMixin:
    paginate_by = 10

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        return context

