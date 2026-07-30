from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from apps.core import views as core_views
from apps.core.sitemap import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}


# Rutas que no necesitan prefijo de idioma.
urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "robots.txt",
        core_views.robots_txt,
        name="robots",
    ),

    path(
        "health/",
        core_views.health,
        name="health",
    ),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]


# Rutas visibles del portafolio.
urlpatterns += i18n_patterns(
    path("", include("apps.core.urls")),
    prefix_default_language=False,
)


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )