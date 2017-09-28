from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/(?P<id>\d+)/$', views.add),
    url(r'^user/(?P<id>\d+)/$', views.display),
    url(r'^remove/(?P<id>\d+)/$', views.remove),
    url(r'^logout/$', views.logout),

]
 