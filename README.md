# Bachkatov Portfolio

A modern portfolio built with **Django**, designed to showcase software engineering projects, cybersecurity research, and artificial intelligence work through a clean, maintainable and scalable architecture.

The project emphasizes modular design, reusable components, structured documentation and long-term maintainability rather than relying on third-party templates or website builders.

---

## Preview

> Screenshots will be added after the first production release.

---

## Features

- Modern and responsive interface
- Component-based template architecture
- Modular CSS architecture
- Context-driven content management
- Reusable UI components
- SEO-ready structure
- Accessibility improvements
- Production-ready project organization

---

## Tech Stack

### Backend

- Python 3
- Django 5

### Frontend

- HTML5
- CSS3
- Vanilla JavaScript

### Development

- Visual Studio Code
- Git
- GitHub

---

## Project Structure

```
apps/
    core/
        context/
        views.py
        urls.py
        context_processors.py

config/
    settings/

docs/

static/
    css/
    js/
    images/
    fonts/
    icons/
    favicon/

templates/
    components/
    layouts/
    pages/
```

---

## Architecture

The project follows a modular Django architecture.

- Content is separated from templates using dedicated context modules.
- Templates are divided into reusable components.
- Styling is organized using a layered CSS architecture.
- Global data is injected through Django Context Processors.
- Static assets are organized by responsibility.

More details are available in:

- `docs/architecture.md`

---

## Documentation

Additional documentation can be found inside the `docs/` directory.

| Document | Description |
|----------|-------------|
| architecture.md | Project architecture |
| coding-standards.md | Coding conventions |
| deployment.md | Production deployment |
| design-system.md | Design guidelines |
| roadmap.md | Project roadmap |

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/Mskre87/bachkatov-portfolio.git
```

### Create a virtual environment

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the development server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## Roadmap

Current development focuses on:

- Production deployment
- Performance optimization
- SEO improvements
- Accessibility improvements
- Publishing software engineering projects
- Publishing cybersecurity research

---

## Status

Current version:

**Version 1.0 (In Development)**

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## Author

**Dimitri Bachkatov**

Software Engineer • Cybersecurity • Artificial Intelligence

GitHub

https://github.com/Mskre87

Future website

https://bachkatov.dev

---

Built with Django and designed for long-term maintainability.