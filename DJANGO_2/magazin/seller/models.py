from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=False, verbose_name="Описание")
    code = models.TextField(blank=False, verbose_name="Код")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время публикации")
    img1 = models.ImageField(upload_to='images', default=None, blank=True, verbose_name="Фото-1")
    img2 = models.ImageField(upload_to='images', default=None, blank=True, verbose_name="Фото-2")
    img3 = models.ImageField(upload_to='images', default=None, blank=True, verbose_name="Фото-3")
    img4 = models.ImageField(upload_to='images', default=None, blank=True, verbose_name="Фото-4")
    img5 = models.ImageField(upload_to='images', default=None, blank=True, verbose_name="Фото-5")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project', kwargs={'project_slug': self.slug})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['title']

class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", null=True)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Reviews(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ваше имя")
    review = models.TextField(blank=False, default=None, verbose_name="Отзыв")
    time_create = models.DateTimeField(auto_now=True, verbose_name="Время публикации")
    star = models.ForeignKey('RatingStar', on_delete=models.CASCADE, verbose_name="звезда", null=True)

    def __str__(self):
        return self.name

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


