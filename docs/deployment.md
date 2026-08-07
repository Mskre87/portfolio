# Deployment

## Overview

Bachkatov Portfolio is deployed as a production Django application on **Railway** and served through the custom domain:

```text
https://bachkatov.dev
```

The repository keeps development and production configuration separated through dedicated Django settings modules.

---

## Production Topology

```text
GitHub Repository
      │
      ▼
Railway
      │
      ├── Railpack build
      │     └── collectstatic
      │
      └── Django application
             │
             ├── migrate
             ├── Gunicorn
             ├── WhiteNoise static files
             └── /health/ healthcheck
      │
      ▼
bachkatov.dev
```

---

## Environment Configuration

The project separates configuration using:

```text
config/settings/
├── base.py
├── development.py
└── production.py
```

Production runs with `DEBUG = False` and uses environment variables for deployment-sensitive configuration.

Sensitive values must remain outside the repository.

---

## Railway Build

The verified Railway configuration uses **Railpack**.

Build command:

```text
python manage.py collectstatic --noinput
```

Static assets are collected before application startup.

---

## Production Process

The current Railway start command performs database migrations and then starts Gunicorn:

```text
python manage.py migrate --noinput
→ gunicorn config.wsgi:application
```

Current Gunicorn deployment settings include:

```text
workers: 2
timeout: 120 seconds
```

The application binds to Railway's assigned `$PORT`.

---

## Health Check

Railway checks:

```text
/health/
```

The deployment configuration allows Railway's internal healthcheck to return successfully without being redirected by the application's HTTPS enforcement.

---

## Restart Policy

The verified Railway deployment configuration uses:

```text
ON_FAILURE
```

with a maximum of three restart retries.

---

## Static Files

Static files are managed through Django's staticfiles system and **WhiteNoise**.

The configured storage backend is:

```text
CompressedManifestStaticFilesStorage
```

This provides compressed, manifest-based static asset handling in production.

---

## Database

The current application configuration uses SQLite:

```text
db.sqlite3
```

The portfolio does not currently require a separate managed relational database service for its public content model.

---

## HTTPS and Browser Security

Railway terminates HTTPS before forwarding requests to Django.

The production settings include:

- HTTPS redirection
- secure session cookies
- secure CSRF cookies
- HSTS
- HSTS subdomain coverage
- HSTS preload
- content-type sniffing protection
- strict referrer policy
- clickjacking protection through `X-Frame-Options: DENY`

---

## Allowed Hosts

Production is configured for:

```text
bachkatov.dev
www.bachkatov.dev
Railway application domains
Railway healthcheck infrastructure
```

The exact deployment hostname assigned by Railway can vary and does not need to be hard-coded into public documentation.

---

## Localization

The production application supports:

```text
English
Spanish
```

Translations are maintained under:

```text
locale/
```

---

## Media

The current portfolio does not rely on user-uploaded production media.

Project assets, images, fonts and documents are maintained as versioned static assets.

---

## Public Repository Boundary

Production secrets must not be committed.

The repository includes `.env.example` as a configuration reference, while live environment values remain private to the deployment environment.

---

## Update Model

Application updates follow the Git/GitHub repository and Railway deployment workflow.

The repository remains the source for application code and public documentation, while deployment-specific secrets remain managed outside Git.

---

## Current Deployment Summary

```text
GitHub
→ Railway / Railpack
→ Django 5
→ Gunicorn
→ WhiteNoise
→ bachkatov.dev
```

The current deployment is active and production-facing.

---

## Future Improvements

Potential future deployment improvements include:

- automated test gates before production deployment
- expanded deployment observability
- additional CI/CD validation
- external database migration if future functionality requires it
- CDN integration if traffic or asset requirements justify it

These are future possibilities rather than current production components.
