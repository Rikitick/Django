# Generated by Django 4.0.6 on 2022-08-13 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_reviews_star_delete_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='time_create',
            field=models.DateTimeField(auto_now=True, verbose_name='Время публикации'),
        ),
    ]