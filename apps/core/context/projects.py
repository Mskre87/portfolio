from dataclasses import dataclass


@dataclass(frozen=True)
class Project:
    title: str
    description: str
    status: str
    technologies: list[str]
    github: str | None = None
    demo: str | None = None


PROJECTS = [

    Project(

        title="bachkatov.dev",

        description=(
            "Personal portfolio built with Django, following modern software "
            "engineering practices, reusable components and scalable architecture."
        ),

        status="In Progress",

        technologies=[
            "Django",
            "HTML",
            "CSS",
            "JavaScript",
        ],

    ),

]