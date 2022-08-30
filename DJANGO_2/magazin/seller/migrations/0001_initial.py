# Generated by Django 4.0.6 on 2022-08-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Описание')),
                ('code', models.TextField(verbose_name='Код')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('img1', models.ImageField(blank=True, default=None, upload_to='images', verbose_name='Фото-1')),
                ('img2', models.ImageField(blank=True, default=None, upload_to='images', verbose_name='Фото-2')),
                ('img3', models.ImageField(blank=True, default=None, upload_to='images', verbose_name='Фото-3')),
                ('img4', models.ImageField(blank=True, default=None, upload_to='images', verbose_name='Фото-4')),
                ('img5', models.ImageField(blank=True, default=None, upload_to='images', verbose_name='Фото-5')),
                ('img6', models.ImageField(blank=True, default=None, upload_to='images', verbose_name='Фото-6')),
                ('img7', models.ImageField(blank=True, default=None, upload_to='images', verbose_name='Фото-7')),
                ('img8', models.ImageField(blank=True, default=None, upload_to='images', verbose_name='Фото-8')),
                ('img9', models.ImageField(blank=True, default=None, upload_to='images', verbose_name='Фото-9')),
                ('img10', models.ImageField(blank=True, default=None, upload_to='images', verbose_name='Фото-10')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ваше имя')),
                ('review', models.TextField(default=None, verbose_name='Отзыв')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('star', models.SmallIntegerField(default=0, verbose_name='Звезда')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]