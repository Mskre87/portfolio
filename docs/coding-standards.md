# Coding Standards

## Purpose

This document defines the coding conventions and development standards used throughout the Bachkatov Portfolio project.

The goal is to ensure consistency, readability, maintainability and scalability as the project evolves.

These guidelines apply to all future development.

---

# General Principles

The project follows a simple philosophy:

- Prioritize readability over cleverness.
- Keep the codebase consistent.
- Prefer composition over duplication.
- Separate content from presentation.
- Write code that is easy to maintain.

Every contribution should improve or preserve these principles.

---

# Python Standards

Python code follows the PEP 8 style guide whenever practical.

General rules:

- Use descriptive names.
- Keep functions small.
- Prefer explicit code over implicit behavior.
- Avoid unnecessary abstractions.
- Remove unused imports.

Views should remain lightweight.

Business logic should not be placed inside templates.

---

# Dataclasses

Structured content should be represented using Python dataclasses whenever appropriate.

Examples include:

- Site information
- Navigation
- Projects
- Certifications
- Current focus

Advantages:

- Improved readability
- Better type safety
- Easier maintenance
- Clear project structure

---

# Views

Views should only be responsible for:

- Receiving the request
- Selecting the template
- Returning the response

Views should not:

- Contain presentation logic
- Duplicate global data
- Build large dictionaries manually

Global data belongs inside Context Processors.

---

# Context Processors

Context Processors provide shared information to every template.

Examples include:

- Site metadata
- Navigation
- Projects
- Certifications
- Current focus

Adding duplicated context directly inside views should be avoided.

---

# Templates

Templates should remain clean and presentation-focused.

Templates should:

- Render data
- Include reusable components
- Minimize duplicated markup

Templates should not:

- Contain business logic
- Perform calculations
- Repeat identical HTML structures

---

# Components

Every visual section should exist as an independent component.

Examples:

- Hero
- About
- Projects
- Current Focus
- Certifications
- Footer
- Navbar

Components should have a single responsibility.

---

# UI Components

Reusable interface elements belong inside:

```
templates/components/ui/
```

Examples include:

- Buttons
- Badges
- Cards
- Section titles

Whenever possible, UI elements should be reused instead of duplicated.

---

# CSS Standards

The project follows a layered CSS architecture.

```
Abstracts

↓

Layout

↓

Components

↓

Pages

↓

Utilities
```

Each layer has a clearly defined responsibility.

---

# CSS Naming

File names use kebab-case.

Examples:

```
hero.css

projects.css

section-title.css

current-focus.css
```

Class names follow a component-based naming convention.

Example:

```
.hero

.hero__title

.hero__description

.hero__actions
```

This keeps selectors predictable and easy to navigate.

---

# CSS Rules

General guidelines:

- One component per file.
- Use CSS variables whenever possible.
- Avoid inline styles.
- Keep selectors shallow.
- Prefer Flexbox and Grid.
- Avoid unnecessary specificity.

Animations should remain subtle and purposeful.

---

# HTML Standards

HTML should be:

- Semantic
- Accessible
- Well-indented
- Easy to scan

Prefer semantic elements such as:

- header
- nav
- main
- section
- article
- footer

Accessibility should be considered during implementation.

---

# JavaScript Standards

JavaScript should remain lightweight.

Use JavaScript only when necessary.

Prefer progressive enhancement over complex client-side logic.

Avoid introducing external libraries without a clear benefit.

---

# Static Assets

Static resources should remain organized by category.

```
static/

    css/

    js/

    images/

    fonts/

    icons/

    favicon/

    documents/
```

Assets should never be placed in arbitrary locations.

---

# Documentation

Major architectural decisions should be documented.

Documentation belongs inside:

```
docs/
```

Important project changes should be reflected in the appropriate documentation files.

---

# Git Workflow

Commits should remain small and focused.

Recommended commit prefixes:

```
feat:
```

New functionality.

```
fix:
```

Bug fixes.

```
docs:
```

Documentation.

```
style:
```

Formatting and visual adjustments.

```
refactor:
```

Internal code improvements.

```
chore:
```

Maintenance tasks.

---

# Code Reviews

Before committing, verify:

- Code is readable.
- No unused code remains.
- Naming is consistent.
- Formatting is correct.
- Documentation is updated when necessary.

---

# Future Development

Future additions should follow the existing architecture instead of introducing parallel patterns.

When adding new functionality:

- Reuse existing components.
- Reuse Context Processors when appropriate.
- Maintain the current directory structure.
- Preserve consistency across the project.

---

# Philosophy

This project values clarity over complexity.

The objective is not to write the shortest code possible, but to create a codebase that remains understandable months or years after it was written.

Every file should have a clear purpose.

Every component should solve one problem.

Every design decision should improve maintainability.

The architecture should continue to evolve without sacrificing simplicity.