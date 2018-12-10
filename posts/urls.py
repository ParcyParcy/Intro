from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_detail, name="post_detail"),
    url(r'^contact/$', views.contact, name='contact'),

]

