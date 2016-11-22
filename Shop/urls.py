from django.conf.urls import patterns, url
from Shop import views

urlpatterns = [
    url(r'^shop(/?)$', views.ShopView.as_view()),
]