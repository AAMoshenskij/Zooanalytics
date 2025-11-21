# superset_config.py
import os
from typing import Any

FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_RBAC": True,
}

# Secret key for session signing
SECRET_KEY = "your-secret-key-here"

# Enable CORS
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['*']
}

# Database configuration
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@db:5432/abd2_db'

# Cache configuration
CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0',
}

DATA_CACHE_CONFIG = CACHE_CONFIG

# Additional settings
PUBLIC_ROLE_LIKE = 'Gamma'
WTF_CSRF_ENABLED = False
TALISMAN_ENABLED = False