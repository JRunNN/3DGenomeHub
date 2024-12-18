from django.urls import path
from .views import *

urlpatterns = [
    path('get_samples/', get_samples, name='get_samples'),
    path('get_enhancers/', get_enhancers, name='get_enhancers'),
    path('get_loops/', get_loops, name='get_loops'),
    path('get_stripes/', get_stripes, name='get_stripes'),
    path('get_compartments/', get_compartments, name='get_compartments'),
    path('get_domain_bound_samples/', get_domain_bound_samples, name='get_domain_bound_samples'),
    # path('task-info/<task_id>/', get_task_info, name='task_info')
]