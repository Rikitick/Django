from django.urls import path
from .views import *

urlpatterns = [
    path('', title, name='home'),
    path('about', about, name='about'),
    path('projects', projects, name='projects'),
    path('contacts', contacts, name='contacts'),
    path('projects/<slug:project_slug>', project, name='project'),
    path('reviews', reviews, name='reviews'),
    path("add-review", AddReview.as_view(), name='add_review'),
]