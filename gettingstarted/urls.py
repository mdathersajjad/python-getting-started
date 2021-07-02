from django.urls import path, include, re_path

from django.contrib import admin
from djproxy.views import HttpProxy


admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    re_path(r'^blog/(?P<url>.*)$', HttpProxy.as_view(base_url='http://testwithoutcache.localhost:3003')),
    re_path(r'^_next/(?P<url>.*)$', HttpProxy.as_view(base_url='http://test-without-cache.localhost:3003/_next/'))
]
