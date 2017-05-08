from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^browse/', include('tgv.urls.browse')),
    url(r'^find/', include('tgv.urls.find')),
    url(r'^inspire/', include('tgv.urls.inspire')),
    url(r'^admin/', admin.site.urls),
    url(r'^gares_list/', include('tgv.urls.gares_list')),
]
