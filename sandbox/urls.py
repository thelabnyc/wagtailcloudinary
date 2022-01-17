from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.urls import path, re_path, include
from django.contrib import admin
from django.conf import settings

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from wagtailcloudinary import site
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

import os


api_router = WagtailAPIRouter("wagtailapi")
api_router.register_endpoint("pages", PagesAPIViewSet)
api_router.register_endpoint("images", ImagesAPIViewSet)
api_router.register_endpoint("documents", DocumentsAPIViewSet)

urlpatterns = [
    url(r"^api/v2/", api_router.urls),
    url(r"^api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    re_path(r"^wagtailcloudinary/", include(site.urls, namespace="wagtailcloudinary")),
    re_path(r"^cms/", include(wagtailadmin_urls)),
    re_path(r"^documents/", include(wagtaildocs_urls)),
    re_path(r"^pages/", include(wagtail_urls)),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL + "images/",
        document_root=os.path.join(settings.MEDIA_ROOT, "images"),
    )
