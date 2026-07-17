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
            "Developing modern web applications with Django while "
            "improving software architecture, clean code and system design."
        ),

    ),

    FocusArea(

        status="Learning",

        title="Cybersecurity",

        description=(
            "Expanding my offensive security knowledge through bug bounty "
            "programs, vulnerability research and secure software practices."
        ),

    ),

    FocusArea(

        status="Exploring",

        title="Artificial Intelligence",

        description=(
            "Studying data science, machine learning and AI engineering "
            "through IBM certifications and personal projects."
        ),

    ),

)