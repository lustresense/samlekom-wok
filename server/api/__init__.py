"""
SIMRP API Package
Modular API endpoints.
"""
from api.auth import auth_routes
from api.events import event_routes
from api.reports import report_routes
from api.geographic import geographic_routes
from api.xp import xp_routes
from api.collaboration import collaboration_routes
from api.admin import admin_routes

__all__ = [
    "auth_routes",
    "event_routes",
    "report_routes",
    "geographic_routes",
    "xp_routes",
    "collaboration_routes",
    "admin_routes",
]
