# Generated by Django 3.0.4 on 2020-03-08 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RecomendedDiet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Disease')),
                ('foodtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.FoodType')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='FoodList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_food', models.CharField(max_length=120)),
                ('foodtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.FoodType')),
            ],
        ),
        migrations.CreateModel(
            name='FoodDiet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.FoodList')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Meal')),
            ],
        ),
    ]
