# Generated by Django 4.0.6 on 2022-08-24 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0016_alter_reviews_star'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='star',
            new_name='star_id',
        ),
    ]
