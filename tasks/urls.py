from django.urls import path
from tasks.views import *
urlpatterns = [
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/', user_dashboard),
   
]