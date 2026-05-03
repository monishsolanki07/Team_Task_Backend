from django.urls import path
from .views import create_project, add_member, project_detail,project_list_create

urlpatterns = [
    path('', project_list_create),
    path('<int:project_id>/add-member/', add_member),
    path('<int:project_id>/', project_detail),
]