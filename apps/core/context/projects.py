from dataclasses import dataclass


@dataclass(frozen=True)
class Project:
    title: str
    description: str
    technologies: tuple[str, ...]
    status: str
    role: str
    timeline: str
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

        technologies=(
            "Django",
            "HTML",
            "CSS",
            "JavaScript",
        ),

        role="Full Stack Developer",

        timeline="2026 – Present",

        github=None,

        demo=None,

    ),

    Project(

        title="Finis Trabaja",

        description=(
            "University job platform developed with Flask and SQL Server, "
            "connecting students and companies through a recruitment portal."
        ),

        technologies=(
            "Python",
            "Flask",
            "SQL Server",
            "HTML",
            "CSS",
            "JavaScript",
        ),

        status="Completed",

        role="Full Stack Developer",

        timeline="2026",

        github=None,

        demo=None,

    ),
]