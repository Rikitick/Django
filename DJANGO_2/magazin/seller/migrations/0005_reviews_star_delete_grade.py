# Generated by Django 4.0.6 on 2022-08-13 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_remove_reviews_star_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='star',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='seller.ratingstar', verbose_name='звезда'),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
