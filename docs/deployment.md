# Deployment

## Overview

This document describes the deployment process for the Bachkatov Portfolio.

The project is designed to support both development and production environments while keeping configuration simple and maintainable.

---

# Requirements

Before deploying, ensure the following requirements are met:

- Python 3
- Django 5
- Git
- Virtual environment
- Production-ready web server
- HTTPS support
- Registered domain name

---

# Environment Configuration

The project separates configuration using dedicated settings modules.

```
config/settings/

    base.py

    development.py

    production.py
```

Each environment should use the appropriate configuration.

Sensitive information should never be committed to the repository.

Examples include:

- Secret Key
- Database credentials
- Email credentials
- API keys

Environment variables should be used whenever possible.

---

# Static Files

Before deployment, collect static files.

```bash
python manage.py collectstatic
```

The deployment platform should serve static assets efficiently.

---

# Media Files

The project currently does not rely on user-uploaded media.

The media directory is reserved for future functionality.

---

# Database

Development currently uses SQLite.

Future production deployments may use:

- PostgreSQL
- MySQL

The architecture does not depend on a specific database engine.

---

# Security Checklist

Before deployment verify:

- DEBUG=False
- SECRET_KEY stored securely
- ALLOWED_HOSTS configured
- HTTPS enabled
- Security headers enabled
- Static files configured correctly

---

# Domain

Primary production domain:

```
bachkatov.dev
```

Future subdomains may include:

- blog.bachkatov.dev
- research.bachkatov.dev

---

# Email

The production environment will use a custom domain email.

Example:

```
contact@bachkatov.dev
```

Email configuration should remain outside the repository.

---

# Performance

Recommended production optimizations include:

- WebP images
- Browser caching
- Compressed static assets
- Lazy loading
- Local font hosting

---

# SEO

Production deployments should include:

- sitemap.xml
- robots.txt
- Open Graph metadata
- Favicon package
- Meta descriptions

---

# Monitoring

After deployment verify:

- No broken links
- No missing static files
- HTTPS certificate
- Mobile responsiveness
- Lighthouse score
- Console errors

---

# Deployment Checklist

Before publishing a new version:

- Update documentation
- Review changelog
- Run Django system checks
- Test responsive layout
- Verify static assets
- Review metadata
- Test navigation
- Verify accessibility

---

# Future Improvements

Possible future deployment improvements include:

- CI/CD
- Automated testing
- Docker support
- CDN integration
- Automated backups

---

# Conclusion

The deployment process prioritizes reliability, security and maintainability.

Every production release should follow this checklist to ensure a consistent and professional deployment.