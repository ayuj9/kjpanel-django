# Generated by Django 4.2.13 on 2024-09-25 01:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('diet_language', models.CharField(max_length=255, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('diet_preference', models.CharField(choices=[('Vegetarian', 'Veg'), ('Non-Vegetarian', 'Non-Veg'), ('Vegan', 'Vegan')], max_length=15)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('recipieLink', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='kjapp/images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='kjapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Diet_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_Time', models.JSONField(blank=True, null=True)),
                ('day1', models.JSONField(blank=True, null=True)),
                ('day2', models.JSONField(blank=True, null=True)),
                ('day3', models.JSONField(blank=True, null=True)),
                ('day4', models.JSONField(blank=True, null=True)),
                ('day5', models.JSONField(blank=True, null=True)),
                ('day6', models.JSONField(blank=True, null=True)),
                ('day7', models.JSONField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateField(verbose_name='Date')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diet', to='kjapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Client_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_plan_updated_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('plan_level', models.CharField(choices=[('B', 'Bronze'), ('S', 'Silver'), ('G', 'Gold')], max_length=20)),
                ('status', models.CharField(choices=[('Created', 'Create'), ('Active', 'Activate'), ('Paused', 'Pause'), ('Suspended', 'Suspend'), ('Expired', 'Expire')], max_length=20)),
                ('duration', models.IntegerField()),
                ('count_down', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='kjapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Client_Insights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_weight', models.CharField(max_length=10, null=True)),
                ('height', models.CharField(max_length=10)),
                ('current_weight', models.CharField(max_length=10)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_plan_updated_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('persona', models.CharField(blank=True, max_length=50, null=True)),
                ('height_Unit', models.CharField(default='inch', max_length=6)),
                ('weight_Unit', models.CharField(default='kg', max_length=2)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insights', to='kjapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('zone', models.CharField(blank=True, max_length=255)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='kjapp.client')),
            ],
        ),
    ]
