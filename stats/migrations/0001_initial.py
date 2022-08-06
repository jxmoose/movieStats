# Generated by Django 4.0.5 on 2022-07-11 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=20)),
                ('actor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=20)),
                ('director', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.UUIDField()),
                ('tconst', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True)),
                ('releaseDate', models.DateField()),
                ('watchDate', models.DateField(default=None, null=True)),
                ('numVotes', models.BigIntegerField(default=0)),
                ('imdbRating', models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Writers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=20)),
                ('writer', models.CharField(max_length=100)),
            ],
        ),
    ]