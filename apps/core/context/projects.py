from dataclasses import dataclass

from django.utils.functional import Promise
from django.utils.translation import gettext_lazy as _


TranslatableText = str | Promise


@dataclass(frozen=True)
class Project:
    title: str
    description: TranslatableText
    technologies: tuple[str, ...]
    status: TranslatableText
    role: TranslatableText
    timeline: TranslatableText
    github: str | None = None
    demo: str | None = None
    featured: bool = False
    github_label: TranslatableText = "GitHub"


PROJECTS = [

    Project(
        title="Phantom Ecosystem",

        description=_(
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

        status=_("Operational"),

        role=_("Creator & Software Engineer"),

        timeline=_("2026 – Present"),

        github="https://github.com/Mskre87/Phantom_Ecosystem",

        demo=None,

        featured=True,

        github_label=_("View Documentation"),
    ),

    Project(
        title="Phantom Leviathan",

        description=_(
            "Autonomous Web3 security research system for continuous public "
            "smart-contract repository monitoring and dynamic analysis. It "
            "combines Forge and Echidna fuzzing with invariant testing, "
            "rotating target discovery and AI-assisted compilation-environment "
            "recovery. The public repository documents the architecture while "
            "the production runtime remains private."
        ),

        technologies=(
            "Python",
            "Docker",
            "Docker Compose",
            "Foundry",
            "Forge",
            "Echidna",
            "Web3",
            "Ollama",
        ),

        status=_("Operational"),

        role=_("Creator & Software Engineer"),

        timeline=_("2026 – Present"),

        github="https://github.com/Mskre87/Phantom-Leviathan",

        demo=None,

        featured=True,

        github_label=_("View Documentation"),
    ),

    Project(
        title="Phantom Hydra",

        description=_(
            "Autonomous semantic fuzzing and LLM red-teaming system for "
            "authorized AI security research. Hydra uses local AI-assisted "
            "mutation and semantic response evaluation, target-specific request "
            "adaptation, configurable routing and automated research triage. "
            "The public repository documents the architecture while the "
            "operational runtime and research corpus remain private."
        ),

        technologies=(
            "Python",
            "asyncio",
            "Ollama",
            "LLM Security",
            "httpx",
            "Cloudflare Workers",
            "Discord",
        ),

        status=_("Operational"),

        role=_("Creator & Software Engineer"),

        timeline=_("2026 – Present"),

        github="https://github.com/Mskre87/Phantom-Hydra",

        demo=None,

        featured=True,

        github_label=_("View Documentation"),
    ),

    Project(
        title="bachkatov.dev",

        description=_(
            "Personal portfolio engineered with Django using a modular "
            "architecture, reusable components and modern frontend practices. "
            "Deployed in production to showcase software engineering projects, "
            "cybersecurity research, artificial intelligence work and "
            "continuous learning."
        ),

        technologies=(
            "Python",
            "Django",
            "HTML",
            "CSS",
            "JavaScript",
        ),

        status=_("Live"),

        role=_("Full Stack Developer"),

        timeline=_("2026 – Present"),

        github="https://github.com/Mskre87/portfolio",

        demo="https://bachkatov.dev",

        featured=False,

        github_label=_("View Source"),
    ),

    Project(
        title="Finis Trabaja",

        description=_(
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

        status=_("Completed"),

        role=_("Full Stack Developer"),

        timeline="2026",

        github=None,

        demo=None,
    ),

]
