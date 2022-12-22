from django.urls import path
from . import views


app_name = 'cafe_core_app'
urlpatterns = [
    path('', views.menu, name='menu'),
    path('menu', views.menu, name='menu'),
    path('stats', views.stats, name='stats'),
    path('user_stats', views.user_stats, name='user_stats'),
    path('user_stats_by_cat', views.user_stats_by_cat, name='user_stats_by_cat'),
    path('select_users_count', views.select_users_count, name='select_users_count'),
    path('user_stats_by/<meal_type>/<num>', views.user_stats_by, name='user_stats_by'),
    path('<meal_category>', views.meal_category, name='meal_category'),
    path('<int:meal_id>/meal', views.meal, name='meal'),
    path('<int:meal_id>/meal_stats', views.meal_statistics, name='meal_statistics'),
    path('<int:meal_id>/meal_stats/chart/', views.chart, name='chart'),
]