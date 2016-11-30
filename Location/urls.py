from django.conf.urls import patterns, url
from Location import views

urlpatterns = [
    url(r'^location/$', views.LocationView.as_view()),
]