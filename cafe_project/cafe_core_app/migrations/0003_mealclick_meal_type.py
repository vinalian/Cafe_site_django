# Generated by Django 4.1.4 on 2022-12-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_core_app', '0002_mealclick_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealclick',
            name='meal_type',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]