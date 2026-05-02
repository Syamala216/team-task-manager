from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create-workspace/', views.create_workspace, name='create_workspace'),
    path('create-task/', views.create_task, name='create_task'),

    # 🔥 NEW LINE (ADD THIS)
    path('update-status/<int:task_id>/<str:status>/', views.update_status, name='update_status'),
]