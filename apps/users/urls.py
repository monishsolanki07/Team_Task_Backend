from django.urls import path
from .views import signup, login,list_users

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('all/', list_users),
]