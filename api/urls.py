from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='welcome.html'), name='api-welcome'),
    path('mining-data/', MiningDataListView.as_view(), name='mining-data'),
]

    