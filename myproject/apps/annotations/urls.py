from django.urls import path
from .views import get_task_info, file_upload

urlpatterns = [
    # path('', AnnotationView.as_view()),
    # path('upload/', FileUploadView.as_view()),
    # path('start-adding/', start_adding_random_numbers, name='start_adding'),
    path('upload/', file_upload, name='file_upload'),
    path('task-info/<task_id>/', get_task_info, name='task_info')
    # path('anno-res/<task_id>/', AnnotationResultListView.as_view())
]