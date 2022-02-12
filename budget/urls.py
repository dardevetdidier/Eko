from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.budget, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
]
