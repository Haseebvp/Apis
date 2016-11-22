from django.conf.urls import patterns, url
from Users import views

urlpatterns = [
    url(r'^users/$', views.Userview.as_view()),
    url(r'^user/(?P<pk>[0-9]+)(/?)$', views.GetUserview.as_view()),

]