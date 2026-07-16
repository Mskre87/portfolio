from .context.site import SITE
from .context.navigation import NAVIGATION
from .context.projects import PROJECTS
from .context.certifications import CERTIFICATIONS

def site_context(request):
    return {
        "site": SITE,
        "navigation": NAVIGATION,
        "projects": PROJECTS,
        "certifications": CERTIFICATIONS,
    }