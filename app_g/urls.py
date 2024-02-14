from django.urls import path
from app_g import views

urlpatterns = [
    path("", views.inicio),
    path("cursos/", views.cursos)
]
