from django.urls import path
from . import views



urlpatterns = [
    path('news_create/', views.news_create_view),
    path('car_create/', views.car_create_view)
]
