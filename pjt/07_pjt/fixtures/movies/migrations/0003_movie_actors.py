# Generated by Django 3.2.18 on 2023-04-21 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_movie_id_review_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.actor'),
            preserve_default=False,
        ),
    ]
