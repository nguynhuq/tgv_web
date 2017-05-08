from django.conf.urls import url
from tgv import views


urlpatterns = [
    url(r'^$', views.gares_list, name='gares_list'),
]