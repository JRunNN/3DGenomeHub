from django.urls import path
from .views import ChromLoopsCancerListView, NonCodingElementSVListView, NonCodingElementSNVListView

urlpatterns = [
    path('cancerloops', ChromLoopsCancerListView.as_view()),
    path('noncodingsv', NonCodingElementSVListView.as_view()),
    path('noncodingsnv', NonCodingElementSNVListView.as_view())
]