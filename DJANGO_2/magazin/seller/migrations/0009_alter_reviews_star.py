# Generated by Django 4.0.6 on 2022-08-24 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0008_alter_reviews_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='star',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='seller.ratingstar', verbose_name='звезда'),
        ),
    ]
