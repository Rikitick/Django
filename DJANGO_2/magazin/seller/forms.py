from django import forms
from .models import Project, Reviews, RatingStar
from django.core.exceptions import ValidationError


class AddProdect(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Project
        fields = ['title', 'slug', 'content', 'code', 'img1', 'img2', 'img3', 'img4', 'img5', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'code': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

    def clean_img1(self):
        img = self.cleaned_data['img1']
        if img is None:
            raise ValidationError('Должна быть как минимум 1 картинка с проектом')

class FormAddReview(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Reviews
        fields = ["name", "review", ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'review': forms.Textarea(attrs={'cols': 100, 'rows': 15}),
        }

class GradeForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Reviews
        fields = ("star", )