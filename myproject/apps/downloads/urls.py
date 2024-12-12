from django.urls import path
from .views import ChromatinInteractionsExportView

urlpatterns = [
    path('chromloops', ChromatinInteractionsExportView.as_view()),
]