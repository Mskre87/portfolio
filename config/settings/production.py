from decouple import config

from .base import *


def csv_list(value: str) -> list[str]:
    return [
        item.strip()
        for item in value.split(",")
        if item.strip()
    ]


DEBUG = False


ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default=(
        ".up.railway.app,"
        "healthcheck.railway.app,"
        "bachkatov.dev,"
        "www.bachkatov.dev"
    ),
    cast=csv_list,
)


CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",
    default=(
        "https://*.up.railway.app,"
        "https://bachkatov.dev,"
        "https://www.bachkatov.dev"
    ),
    cast=csv_list,
)


# Railway terminates HTTPS before forwarding traffic to Django.
SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

SECURE_SSL_REDIRECT = True

# Railway's internal healthcheck must return HTTP 200.
SECURE_REDIRECT_EXEMPT = [
    r"^health/$",
]


# Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# HTTPS and browser security
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

X_FRAME_OPTIONS = "DENY"