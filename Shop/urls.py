from django.conf.urls import patterns, url
from Shop import views

urlpatterns = [
    url(r'^shop(/?)$', views.ShopView.as_view()),
    url(r'^signup/$', views.SignUp.as_view()),
    url(r'^login/$', views.Login.as_view()),
    url(r'^query/$', views.UserQuery.as_view()),
]