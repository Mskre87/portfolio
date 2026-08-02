from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):

    priority = 1.0
    changefreq = "monthly"

    i18n = True
    languages = ("en", "es")

    alternates = True
    x_default = True

    def items(self):
        return [
            "home",
        ]

    def location(self, item):
        return reverse(item)