from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('accounts/', views.view_accounts, name='accounts'),
    path('delete-account/', views.delete_account, name='delete-account'),
    path('update-operation/<str:pk>/', views.update_operation, name='update-operation'),
    path('delete-operation/<str:pk>/', views.delete_operation, name='delete-operation'),
    path('categories/', views.view_categories, name='categories'),
    path('delete-category/<str:pk>/', views.delete_category, name='delete-category'),
]
