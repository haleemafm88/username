from django.urls import path
from form import views

urlpatterns = [
        path('result/', views.result, name='result'),
        path('home/',views.home, name='home'),
]
