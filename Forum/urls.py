from django.conf.urls import url
from .views import *

app_name = 'forum'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<page_number>[0-9]+)$', index, name='index'),
    url(r'^topic/(?P<pk>[0-9]+)/(?P<page_number>[0-9]+)', topic, name='topic'),
    url(r'^login/', log_in, name='log_in'),
    url(r'^register/', register, name='register'),
    url(r'^logout/', log_out, name='log_out'),
]