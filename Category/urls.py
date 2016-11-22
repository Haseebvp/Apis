from django.conf.urls import patterns, url
from Category import views

urlpatterns = [
    url(r'^getmaincategory/$', views.MainCategoryview.as_view()),
    url(r'^getcategory/$', views.Categoryview.as_view()),
    url(r'^getsubcategory/$', views.SubCategoryview.as_view()),
    url(r'^getcategory/(?P<pk>[0-9]+)(/?)$', views.SingleCategory.as_view()),
    url(r'^getsubcategory/(?P<pk>[0-9]+)(/?)$', views.SingleSubCategory.as_view()),

]