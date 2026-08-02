from dataclasses import dataclass

from django.utils.functional import Promise
from django.utils.translation import gettext_lazy as _


TranslatableText = str | Promise


@dataclass(frozen=True)
class Site:
    # General

    name: str
    domain: str
    language: str
    locale: str
    author: str

    # Branding

    tagline: TranslatableText
    footer_tagline: TranslatableText
    copyright: TranslatableText

    # SEO

    description: TranslatableText
    keywords: TranslatableText
    theme_color: str
    og_image: str

    # Contact

    email: str

    # Social

    github: str
    linkedin: str
    credly: str
    hackerone: str
    intigriti: str

    # Documents

    resume: str


SITE = Site(

    # General

    name="Bachkatov",

    domain="bachkatov.dev",

    language="en",

    locale="en_US",

    author="Dimitri Bachkatov",

    # Branding

    tagline=_(
        "Building software, uncovering vulnerabilities, "
        "and engineering secure digital experiences."
    ),

    footer_tagline=_(
        "Building secure software, exploring cybersecurity "
        "and engineering intelligent systems."
    ),

    copyright=_(
        "© 2026 Dimitri Bachkatov. All rights reserved."
    ),

    # SEO

    description=_(
        "Software Engineering student focused on Cybersecurity "
        "and Artificial Intelligence."
    ),

    keywords=_(
        "Software Engineering Student, Cybersecurity, Artificial Intelligence, "
        "Python, Django, Portfolio, Security Research"
    ),

    theme_color="#050505",

    og_image="/static/images/og/og-image.png",

    # Contact

    email="contact@bachkatov.dev",

    # Social

    github="https://github.com/Mskre87",

    linkedin="https://linkedin.com/in/dimitri-bachkatov-droguett-825986312/",

    credly="https://www.credly.com/users/dimitri-bachkatov",

    hackerone="",

    intigriti="",

    # Documents

    resume="documents/dimitri-bachkatov-resume.pdf",
)