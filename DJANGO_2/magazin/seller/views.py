from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.base import View
from django.views.decorators.cache import cache_page
from .forms import FormAddReview, GradeForm
from .models import Project, Reviews
from .utils import DataMixin


def pageNotFound(req, exception):
    return render(req, 'seller/error.html', {'exception': exception})


def title(req):
    return render(req, 'seller/index.html', {'title': 'Главная страница'})


def about(req):
    return render(req, 'seller/about.html', {'title': 'Обо мне'})


def contacts(req):
    return render(req, 'seller/my_contacts.html', {'title': 'Мои контакты'})


@cache_page(60 * 10)
def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'title': 'Мои проекты',
    }
    return render(request, 'seller/my_projects.html', context=context)


@cache_page(60 * 10)
def project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    context = {
        'project': project,
        'title': project.title,
    }
    return render(request, 'seller/project.html', context=context)


def reviews(req):
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews,
        'title': 'Отзывы',
    }
    return render(req, 'seller/reviews.html', context=context)


class AddReview(DataMixin, CreateView):
    form_class = FormAddReview
    template_name = 'seller/add_review.html'
    success_url = reverse_lazy('reviews')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = GradeForm()
        c_def = self.get_user_context(title='Добавление отзыва')
        return dict(list(context.items()) + list(c_def.items()))

    def post(self, request):
        r = Reviews(star_id=int(request.POST.get("star")), name=request.POST.get('name'),
                    review=request.POST.get('review'), time_create=request.POST.get('time_create'))
        r.save()
        return redirect("home")
