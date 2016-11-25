from django.conf.urls import patterns, url
from Users import views

urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view()),
    url(r'^login/$', views.Login.as_view()),
    url(r'^user/(?P<pk>[0-9]+)(/?)$', views.UserDetails.as_view()),

]