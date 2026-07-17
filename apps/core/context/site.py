from dataclasses import dataclass


@dataclass(frozen=True)
class Site:

    name: str

    domain: str

    tagline: str

    email: str

    github: str

    linkedin: str

    credly: str

    hackerone: str

    intigriti: str

    resume: str

    copyright: str


SITE = Site(

    name="Bachkatov",

    domain="bachkatov.dev",

    tagline=(
        "Building software, uncovering vulnerabilities, "
        "and engineering secure digital experiences."
    ),

    email="contact@bachkatov.dev",

    github="https://github.com/Mskre87",

    linkedin="",

    credly="https://www.credly.com/users/dimitri-bachkatov",

    hackerone="",

    intigriti="",

    resume="",

    copyright="© 2026 Bachkatov. All rights reserved.",

)