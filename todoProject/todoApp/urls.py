from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.task_list, name='task_list'),
    path('project/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:pk>/complete/', views.complete_task, name='complete_task'),
]

