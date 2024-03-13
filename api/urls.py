from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('api/', TemplateView.as_view(template_name='welcome.html'), name='welcome'),
    path('api/mining-data/', MiningDataListView.as_view(), name='mining-data'),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]

    