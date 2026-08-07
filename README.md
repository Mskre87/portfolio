# Bachkatov Portfolio

A production portfolio built with **Django** to showcase software engineering, cybersecurity research, artificial intelligence work and selected technical projects through a clean, maintainable and scalable architecture.

The project emphasizes modular design, reusable components, structured documentation and long-term maintainability rather than relying on third-party templates or website builders.

---

## Live Website

**Production:** https://bachkatov.dev

**Repository:** https://github.com/Mskre87/portfolio

---

## Featured Work

The portfolio currently highlights independent software engineering and security-research projects, including the main systems developed under **Phantom Platform**:

- **Phantom Ecosystem** — autonomous security research ecosystem composed of 12 specialized services.
- **Phantom Leviathan** — autonomous Web3 smart-contract analysis and dynamic fuzzing system.
- **Phantom Hydra** — autonomous semantic fuzzing and LLM red-teaming system for authorized AI security research.
- **Finis Trabaja** — university recruitment platform built with Flask and SQL Server.
- **bachkatov.dev** — the portfolio platform itself, built and deployed with Django.

The public Phantom repositories contain architecture and technical documentation only; operational runtimes, credentials, private configuration and sensitive research data remain private.

---

## Features

- Modern and responsive interface
- Component-based Django template architecture
- Modular CSS architecture
- Context-driven content management
- Reusable UI components
- English / Spanish localization
- SEO-ready structure
- Accessibility improvements
- Production deployment configuration
- Downloadable technical resume
- Project cards with documentation, source and live-demo links

---

## Tech Stack

### Backend

- Python 3
- Django 5
- Gunicorn

### Frontend

- HTML5
- CSS3
- Vanilla JavaScript

### Production

- WhiteNoise
- Railway

### Development

- Visual Studio Code
- Git
- GitHub

---

## Project Structure

```text
apps/
    core/
        context/
        views.py
        urls.py
        context_processors.py

config/
    settings/

docs/

locale/

static/
    css/
    js/
    images/
    fonts/
    documents/
    favicon/

templates/
    components/
    layouts/
    pages/

resume/
```

---

## Architecture

The project follows a modular Django architecture.

- Content is separated from templates using dedicated context modules.
- Templates are divided into reusable components.
- Styling is organized using a layered CSS architecture.
- Global data is injected through Django Context Processors.
- Static assets are organized by responsibility.
- Environment-specific Django settings separate development and production behavior.

More details are available in `docs/architecture.md`.

---

## Documentation

Additional documentation is maintained inside the `docs/` directory.

| Document | Description |
|---|---|
| `architecture.md` | Project architecture |
| `coding-standards.md` | Coding conventions |
| `deployment.md` | Production deployment |
| `design-system.md` | Design guidelines |
| `roadmap.md` | Project roadmap |

---

## Local Development

### Clone the repository

```bash
git clone https://github.com/Mskre87/portfolio.git
cd portfolio
```

### Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Or on Linux / macOS:

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure the environment

Use `.env.example` as the reference for local environment variables. Do not commit production secrets.

### Run the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

## Status

**Production / Live**

Current public baseline:

**v1.0.0**

The portfolio is actively maintained and continues to evolve as new engineering and security-research projects are published.

---

## Roadmap

Ongoing development focuses on:

- Publishing new software engineering and security-research projects
- Expanding technical project documentation
- Performance optimization
- SEO improvements
- Accessibility improvements
- Technical writing and case studies
- Long-term content and project discoverability

See `docs/roadmap.md` for the long-term project direction.

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## Author

**Dimitri Bachkatov**

Software Engineering • Cybersecurity • Artificial Intelligence

- GitHub: https://github.com/Mskre87
- Website: https://bachkatov.dev

---

Built with Django and designed for long-term maintainability.
