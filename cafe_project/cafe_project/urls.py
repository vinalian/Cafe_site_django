from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.main, name='main'),
    path('cafe_core_app/', include('cafe_core_app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', include('registration.urls')),
    path('accounts/', include('registration.urls'))
]
