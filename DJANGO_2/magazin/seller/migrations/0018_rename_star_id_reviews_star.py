# Generated by Django 4.0.6 on 2022-08-24 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0017_rename_star_reviews_star_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='star_id',
            new_name='star',
        ),
    ]
