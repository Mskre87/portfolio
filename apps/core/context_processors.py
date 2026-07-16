from .context.site import SITE


def site_context(request):
    return {
        "site": SITE,
    }