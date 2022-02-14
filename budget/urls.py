from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('accounts/', views.view_accounts, name='accounts'),
    path('delete-account/', views.delete_account, name='delete-account'),
    path('detail-operation/<str:pk>/', views.detail_operation, name='detail-operation'),
    path('delete-operation/<str:pk>/', views.delete_operation, name='delete-operation')
]
