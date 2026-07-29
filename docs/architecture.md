# Architecture

## Overview

Bachkatov Portfolio is a Django-based personal portfolio designed with a strong emphasis on maintainability, scalability and clean architecture.

Rather than embedding content directly into templates or views, the project separates concerns into independent layers:

- Routing
- View rendering
- Context providers
- Reusable templates
- Layered CSS architecture
- Static assets

This organization allows the portfolio to evolve over time without requiring major structural changes.

---

# Architectural Goals

The project was designed around the following principles:

- Separation of concerns
- Component reusability
- Maintainability
- Scalability
- Readability
- Consistency

Every design decision attempts to improve one or more of these principles.

---

# High-Level Architecture

```
                    Browser
                        │
                        ▼
                  Django URLConf
                        │
                        ▼
                     View
                        │
                        ▼
             Context Processors
                        │
                        ▼
              Django Templates
                        │
                        ▼
             Reusable Components
                        │
                        ▼
                  HTML Response
```

The application renders server-side HTML using Django templates while injecting global content through Context Processors.

---

# Project Structure

```
apps/
config/
docs/
media/
static/
templates/
```

Each directory has a single responsibility.

| Directory | Responsibility |
|-----------|----------------|
| apps | Django applications |
| config | Project configuration |
| docs | Technical documentation |
| static | CSS, JavaScript, images, fonts and icons |
| templates | HTML templates |
| media | User-uploaded media (future use) |

---

# Django Application Structure

The project currently contains a single Django application.

```
apps/

    core/

        context/

        views.py

        urls.py

        context_processors.py
```

The application is intentionally lightweight.

Business logic is minimal because the portfolio primarily renders structured content.

---

# Request Lifecycle

Every request follows the same execution flow.

```
Browser

↓

URL Configuration

↓

View

↓

Context Processors

↓

Template Rendering

↓

Reusable Components

↓

HTML Response
```

This keeps the rendering pipeline simple and predictable.

---

# Routing

Routing is centralized using Django's URL dispatcher.

```
config/urls.py
```

Application-specific routes are delegated to:

```
apps/core/urls.py
```

This separation keeps the project ready for future applications.

---

# Views

Views remain intentionally small.

Their only responsibility is selecting the template to render.

Example:

```
Request

↓

home()

↓

pages/home.html
```

Views do not contain presentation content.

---

# Context Processors

Global information is injected through Django Context Processors.

This eliminates duplicated code across templates.

Examples include:

- Site information
- Navigation links
- Projects
- Certifications
- Current focus

Instead of writing:

```
return render(
    request,
    "...",
    {
        ...
    }
)
```

every view automatically receives the same global context.

---

# Context Modules

Project content is organized inside dedicated modules.

```
apps/core/context/

    site.py

    navigation.py

    projects.py

    current_focus.py

    certifications.py
```

Each module is responsible for a single type of content.

This approach keeps templates completely independent from data storage.

---

# Data Organization

Project data is represented using Python dataclasses.

Advantages include:

- Type safety
- Readability
- Easy maintenance
- Better organization
- Future extensibility

Instead of dictionaries scattered throughout the project, structured objects describe the portfolio content.

---

# Template Architecture

Templates are divided by responsibility.

```
templates/

    base.html

    pages/

    layouts/

    components/
```

The hierarchy follows:

```
Base Template

↓

Page

↓

Components

↓

Reusable UI Elements
```

This minimizes duplicated markup.

---

# Component System

Each visual section is implemented as an independent component.

Examples include:

- Hero
- About
- Projects
- Current Focus
- Certifications
- Footer
- Navbar

Each component is responsible only for its own presentation.

---

# UI Components

Small reusable UI elements live inside:

```
templates/components/ui/
```

Examples:

- Buttons
- Badges
- Cards
- Section titles

These components can be reused anywhere without duplication.

---

# Styling Architecture

The CSS follows a layered architecture.

```
main.css

│

├── Abstracts

├── Layout

├── Components

├── Pages

└── Utilities
```

Each layer has a clear responsibility.

---

## Abstracts

Contains global definitions.

Examples:

- Variables
- Typography
- Reset
- Animations

---

## Layout

Defines page structure.

Examples:

- Containers
- Sections
- Grid

---

## Components

Contains isolated component styles.

Examples:

- Hero
- Navbar
- Footer
- Projects

Each file styles only one component.

---

## Pages

Contains page-specific styles.

Examples:

- Home
- UI showcase

---

## Utilities

Contains helper classes and small reusable utilities.

Examples:

- Reveal animations
- Helper classes
- Accessibility utilities

---

# Static Assets

Static resources are organized by category.

```
static/

    css/

    js/

    images/

    icons/

    fonts/

    favicon/
```

This organization improves discoverability and long-term maintenance.

---

# Design Philosophy

The visual design follows a minimalist approach.

Goals include:

- High readability
- Strong typography
- Consistent spacing
- Limited color palette
- Clear visual hierarchy

The interface intentionally avoids unnecessary decoration.

---

# Scalability

Although currently implemented as a single-page portfolio, the architecture allows future expansion.

Possible additions include:

- Blog
- Research articles
- Project pages
- Case studies
- Admin-managed content
- API endpoints

No significant architectural changes would be required.

---

# Maintainability

The project is designed so that most future updates only require modifying files inside:

```
apps/core/context/
```

rather than editing templates or views.

This significantly reduces maintenance effort.

---

# Future Evolution

Potential future improvements include:

- Database-backed content
- Markdown-based articles
- Search functionality
- Dark/Light themes
- Internationalization
- Project filtering
- CMS integration

The current architecture supports these additions without requiring a redesign.

---

# Conclusion

The architecture prioritizes simplicity, consistency and long-term maintainability.

Rather than optimizing for rapid development, the project focuses on clean organization, reusable components and clear separation of responsibilities.

This foundation allows the portfolio to grow gradually while keeping the codebase understandable and easy to maintain.