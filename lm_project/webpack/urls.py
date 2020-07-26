from django.urls import path, re_path
from . import views
from . import api

urlpatterns = [
    re_path(r'^(.*)/$', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard-landing'),
    path('api/refresh-template', api.refresh_template, name='dashboard-refresh-template')
]
