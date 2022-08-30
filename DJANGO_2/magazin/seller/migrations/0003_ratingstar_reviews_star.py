# Generated by Django 4.0.6 on 2022-08-13 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_remove_reviews_star'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
                'ordering': ['-value'],
            },
        ),
        migrations.AddField(
            model_name='reviews',
            name='star',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='seller.ratingstar', verbose_name='звезда'),
        ),
    ]