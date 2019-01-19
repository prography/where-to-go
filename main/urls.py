from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index_page, name='index'),
]