from dataclasses import dataclass


@dataclass(frozen=True)
class Site:
    # General

    name: str
    domain: str
    language: str
    locale: str
    author: str

    # Branding

    tagline: str
    footer_tagline: str
    copyright: str

    # SEO

    description: str
    keywords: str
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

    tagline=(
        "Building software, uncovering vulnerabilities, "
        "and engineering secure digital experiences."
    ),

    footer_tagline="Building secure software, exploring cybersecurity and engineering intelligent systems.",

    copyright="© 2026 Dimitri Bachkatov. All rights reserved.",

    # SEO

    description=(
        "Software Engineer focused on Software Engineering, "
        "Cybersecurity and Artificial Intelligence."
    ),

    keywords=(
        "Software Engineer, Cybersecurity, Artificial Intelligence, "
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