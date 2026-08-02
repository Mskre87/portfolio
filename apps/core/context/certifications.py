from dataclasses import dataclass

from django.utils.functional import Promise
from django.utils.translation import gettext_lazy as _


TranslatableText = str | Promise


@dataclass(frozen=True)
class Certification:
    issuer: str
    title: TranslatableText
    description: TranslatableText
    url: str
    action: TranslatableText


CERTIFICATIONS = [

    Certification(

        issuer="IBM SkillsBuild",

        title=_("9 Verified Professional Credentials"),

        description=_(
            "Professional certifications covering Python, Data Science, "
            "Data Analysis, Data Visualization, Data Science Foundations "
            "and related technologies."
        ),

        url="https://www.credly.com/users/dimitri-bachkatov",

        action=_("View Credly Profile"),

    ),

    Certification(

        issuer="International English Test",

        title=_("English Proficiency (C1)"),

        description=_(
            "Verified C1 English proficiency for professional and "
            "technical communication."
        ),

        url=(
            "https://internationalenglishtest.com/"
            "verify-certificate/"
            "758B8DE2A1-758B8DE304-758B8DBA6C"
        ),

        action=_("View Certificate"),

    ),

]