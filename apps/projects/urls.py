from django.urls import path
from .views import create_project, add_member

urlpatterns = [
    path('', create_project),
    path('<int:project_id>/add-member/', add_member),
]