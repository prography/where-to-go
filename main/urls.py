from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('home/', views.index_page, name='index'),
    path('select/', views.select_page, name='select'),
]

