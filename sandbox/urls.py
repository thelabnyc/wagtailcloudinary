from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.contrib import admin
from django.conf import settings
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from wagtailcloudinary import site
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^wagtailcloudinary/', include(site.urls, namespace="wagtailcloudinary")),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))

