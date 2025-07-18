from django.urls import path
from tasks.views import *
urlpatterns = [
    path('show-tasks', showTasks),
    path('show-task/<int:id>', showSpecificTask)
]