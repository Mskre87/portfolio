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
    demo: str |None = None
    featured: bool = False
    github_label: str = "GitHub"

PROJECTS = [

    Project(
        title="Phantom Ecosystem",
        description=(
            "Autonomous security research ecosystem composed of 12 "
            "containerized services for web reconnaissance, source-code "
            "intelligence, secret detection, reverse engineering, mobile and "
            "Web3 analysis, CI/CD inspection, DNS reconnaissance and "
            "cross-module event correlation. The public repository contains "
            "the technical architecture and documentation, while the "
            "operational code remains private."
        ),
        technologies=(
            "Python",
            "Docker",
            "Docker Compose",
            "Redis",
            "FastAPI",
            "aiohttp",
            "Ghidra",
            "JADX",
            "Slither",
        ),
        status="Operational",
        role="Creator & Software Engineer",
        timeline="2026 – Present",
        github="https://github.com/Mskre87/Phantom_Ecosystem",
        demo=None,
        featured=True,
        github_label="View Documentation",
    ),

    Project(

        title="bachkatov.dev",

        description=(
            "Personal portfolio engineered with Django using a modular "
            "architecture, reusable components and modern frontend practices. "
            "Designed to showcase software engineering projects, cybersecurity "
            "research and continuous learning."
        ),

        technologies=(
            "Python",
            "Django",
            "HTML",
            "CSS",
            "JavaScript",
        ),

        status="In Progress",

        role="Full Stack Developer",

        timeline="2026 – Present",

        github="https://github.com/Mskre87",

        demo=None,

    ),

    Project(

        title="Finis Trabaja",

        description=(
            "University recruitment platform developed for Universidad Finis "
            "Terrae, connecting students and companies through a centralized "
            "job portal with dedicated experiences for applicants and employers."
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