from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('accounts/', views.view_accounts, name='accounts'),
    path('delete-account/<int:pk>/', views.delete_account, name='delete-account'),
]
