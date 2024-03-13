from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from api.views import get_mining_data


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('', TemplateView.as_view(template_name='welcome.html'), name='home'),
 ]