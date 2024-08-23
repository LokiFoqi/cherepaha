from django.urls import path
from panzer.views import home

urlpatterns = [
    path('', home, name='home'),  # Главная страница
]
