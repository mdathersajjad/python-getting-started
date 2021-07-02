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

class LetterdropProxy(HttpProxy):
    base_url = 'https://sajjad.anchorsms.com'
    proxy_middleware = [
        'djproxy.proxy_middleware.AddXFF',
        'djproxy.proxy_middleware.AddXFH',
        'djproxy.proxy_middleware.AddXFP'
    ]

class LetterdropAssetProxy(HttpProxy):
    base_url = 'https://sajjad.anchorsms.com/_next/'
    proxy_middleware = [
        'djproxy.proxy_middleware.AddXFF',
        'djproxy.proxy_middleware.AddXFH',
        'djproxy.proxy_middleware.AddXFP'
    ]

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    re_path(r'^blog/(?P<url>.*)$', LetterdropProxy.as_view()),
    re_path(r'^_next/(?P<url>.*)$', LetterdropAssetProxy.as_view())
]
