from django.conf.urls import url
# from .views import index
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'(?P<question_id>[0-9]+)/$', views.detail),
    url(r'(?P<question_id>[0-9]+)/results/$', views.results),
    url(r'(?P<question_id>[0-9]+)/vote/$', views.vote),
]