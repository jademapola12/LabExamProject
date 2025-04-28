from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/create/', views.project_create, name='project_create'),
    path('project/<int:pk>/task/create/', views.task_create, name='task_create'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),  
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),  
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('projects/', views.project_list, name='project_list'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
     path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
     path('home/', views.home, name='home')
    
]
 