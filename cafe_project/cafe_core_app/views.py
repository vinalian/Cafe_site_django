from datetime import timedelta
from django.shortcuts import render
from .models import Meal, MealClick
from django.utils import timezone


def menu(request):
    meal_categories = list(filter(lambda el: 'NO_TYPE' not in el[0], Meal.MealType.choices))
    return render(request, 'cafe_core_app/menu.html', {'meal_categories': meal_categories, 'user': request.user})


def meal_category(request, meal_category):
    meals_by_category = Meal.objects.filter(meal_type=meal_category)
    return render(request, 'cafe_core_app/meals.html', {'meals': meals_by_category, 'meal_category': meal_category, 'user': request.user})


def stats(request):
    all_meals = MealClick.objects.filter().distinct('meal_id')
    top_meals = []
    for meal in all_meals:
        top_meals.append([MealClick.objects.filter(meal_id=meal.meal_id).count(),
                         f' {(Meal.objects.get(id=meal.meal_id)).name}'])
    top_meals = sorted(top_meals)[-1:-4:-1]
    return render(request, 'cafe_core_app/stats.html', {'meals': top_meals, 'user': request.user})


def meal(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    meal_type = Meal.objects.filter(id=meal_id).distinct('meal_type')
    meal.mealclick_set.create(click_date=timezone.now(), user_name = request.user, meal_type=meal_type[0].meal_type)
    return render(request, 'cafe_core_app/meal.html', {'meal': meal, 'user': request.user})


def meal_statistics(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    stats = MealClick.objects.filter(meal_id=meal_id).count()
    return render(request, 'cafe_core_app/meal_stats.html', {'meal': meal, 'stats': stats, 'user': request.user})


def user_stats(request):
    users = MealClick.objects.filter().distinct('user_name').exclude(user_name='AnonymousUser')
    disc = ''
    top_users = []
    for user in users:
        print(MealClick.objects.filter(user_name=user.user_name).distinct("user_name"))
        top_users.append([MealClick.objects.filter(user_name=user.user_name).count(),
                          f'{(MealClick.objects.distinct("user_name").get(user_name=user.user_name)).user_name}'])
    top_users = sorted(top_users)[-1:-11:-1]
    if len(top_users) < 10:
        disc += f'Топ {len(top_users)} пользователя(-ей). (Это все зарегестрированные пользователи, которые тут были 😞)'
    else:
        disc += f'Топ {10} пользователей:'
    return render(request, 'cafe_core_app/user_stats.html', {'top_users': top_users, 'disc': disc})


def user_stats_by_cat(request):
    num = request.GET['num']
    cat = Meal.objects.all().distinct('meal_type')
    return render(request, 'cafe_core_app/user_stats_by_cat.html', {'data': cat, 'num': num})


def user_stats_by(request, meal_type, num):
    disc = ''
    top_users = []
    users = MealClick.objects.filter(meal_type=meal_type).distinct('user_name').exclude(user_name='AnonymousUser')
    for user in users:
        top_users.append([MealClick.objects.filter(user_name=user.user_name, meal_type=meal_type).count(),
                          user.user_name])
    top_users = sorted(top_users)[-1:-int(num)-1:-1]
    if len(top_users) < int(num):
        disc += f'Всего {len(top_users)} пользователя(-ей) заходили в эту категорию. Вот они:'
    else:
        disc += f'Топ { num } пользователей в категории { meal_type }:'
    return render(request, 'cafe_core_app/user_stats_by.html', {'users': top_users, 'meal_type': meal_type, 'num': num, 'disc': disc})


def select_users_count(request):
    return render(request, 'cafe_core_app/select_users_count.html')


def chart(request, meal_id):
    today = timezone.now()
    yesterday = today - timedelta(days=1)
    week = today - timedelta(days=7)
    all_date = []
    click = set()
    redy_date = []
    if request.GET['chart'] == '1':                                                               #day
        for date in MealClick.objects.filter(click_date__gt=yesterday):
            all_date.append(date.click_date.hour)
        for times in all_date:
            click.add(f'{times}*{all_date.count(times)}')
    else:                                                                                       # week
        for date in MealClick.objects.filter(click_date__gt=week):
            all_date.append(date.click_date.day)
        for times in all_date:
            click.add(f'{times}*{all_date.count(times)}')
    sorted(click)
    for i in click:
        redy_date.append([int(i.split('*')[0]), int(i.split('*')[1])])
    return render(request, 'cafe_core_app/chart.html', {'date': sorted(redy_date)})