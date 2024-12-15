from django.urls import path
from .views import *

urlpatterns = [
    path('get_samples/', get_samples, name='get_samples'),
    # path('task-info/<task_id>/', get_task_info, name='task_info')
]