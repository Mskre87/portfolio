from dataclasses import dataclass


@dataclass(frozen=True)
class FocusArea:
    status: str
    title: str
    description: str


CURRENT_FOCUS = (

    FocusArea(

        status="Building",

        title="Software Engineering",

        description=(
            "Building modern web applications with Django while strengthening "
            "software architecture, clean code, reusable components and "
            "scalable system design."
        ),

    ),

    FocusArea(

        status="Learning",

        title="Cybersecurity",

        description=(
            "Developing practical offensive security skills through bug bounty "
            "programs, web application testing, secure development practices "
            "and vulnerability research."
        ),

    ),

    FocusArea(

        status="Exploring",

        title="Artificial Intelligence",

        description=(
            "Exploring data science, machine learning and AI engineering "
            "through IBM professional certifications and hands-on projects."
        ),

    ),

)