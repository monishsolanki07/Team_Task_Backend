from django.urls import path
from .views import create_task, my_tasks, update_task, dashboard,calendar_view,task_activity

urlpatterns = [
    path('', create_task),
    path('my/', my_tasks),
    path('<int:id>/', update_task),
    path('dashboard/', dashboard),
    path('calendar/', calendar_view),
    path('<int:task_id>/activity/', task_activity),
]