from django.conf.urls import url
from tgv import views


urlpatterns = [
    url(r'^$', views.find, name='find'),
]
