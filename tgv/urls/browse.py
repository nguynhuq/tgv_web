from django.conf.urls import url
from tgv import views


urlpatterns = [
    url(r'^$', views.browse, name='browse'),
]