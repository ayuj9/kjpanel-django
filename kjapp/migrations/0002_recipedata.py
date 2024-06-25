# Generated by Django 5.0.4 on 2024-06-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kjapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('recipieLink', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
