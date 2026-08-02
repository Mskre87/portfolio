from dataclasses import dataclass

from django.utils.functional import Promise
from django.utils.translation import gettext_lazy as _


TranslatableText = str | Promise


@dataclass(frozen=True)
class FocusArea:
    status: TranslatableText
    title: TranslatableText
    description: TranslatableText


CURRENT_FOCUS = (

    FocusArea(

        status=_("Building"),

        title=_("Software Engineering"),

        description=_(
            "Building modern web applications with Django while strengthening "
            "software architecture, clean code, reusable components and "
            "scalable system design."
        ),

    ),

    FocusArea(

        status=_("Learning"),

        title=_("Cybersecurity"),

        description=_(
            "Developing practical offensive security skills through bug bounty "
            "programs, web application testing, secure development practices "
            "and vulnerability research."
        ),

    ),

    FocusArea(

        status=_("Exploring"),

        title=_("Artificial Intelligence"),

        description=_(
            "Exploring data science, machine learning and AI engineering "
            "through IBM professional certifications and hands-on projects."
        ),

    ),

)