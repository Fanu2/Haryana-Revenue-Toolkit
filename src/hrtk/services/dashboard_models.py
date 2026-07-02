"""
dashboard_models.py
===================

Data models used by the DashboardService.

These classes are intentionally independent of Qt and persistence.
They provide a clean contract between the service layer and the
presentation layer.

The dashboard should never expose repositories or ORM objects to the UI.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


# ----------------------------------------------------------------------
# Workspace
# ----------------------------------------------------------------------

@dataclass(slots=True)
class WorkspaceInfo:
    """
    Information about the currently active workspace.
    """

    village: str = ""
    jamabandi_year: str = ""
    district: str = ""
    tehsil: str = ""
    office: str = ""
    database: str = ""
    user: str = ""
    workspace_name: str = ""


# ----------------------------------------------------------------------
# Summary Cards
# ----------------------------------------------------------------------

@dataclass(slots=True)
class SummaryCard:
    """
    Dashboard summary card.
    """

    key: str
    title: str
    value: int = 0

    subtitle: str = ""
    icon: str = ""
    color: str = ""
    route: str = ""

    enabled: bool = True


# ----------------------------------------------------------------------
# Validation
# ----------------------------------------------------------------------

@dataclass(slots=True)
class ValidationSummary:
    """
    Overall health of the application data.
    """

    healthy: int = 0
    warnings: int = 0
    errors: int = 0

    message: str = ""


# ----------------------------------------------------------------------
# Recent Activity
# ----------------------------------------------------------------------

@dataclass(slots=True)
class ActivityItem:
    """
    Single activity entry.
    """

    title: str
    description: str = ""
    timestamp: str = ""
    icon: str = ""
    category: str = ""


# ----------------------------------------------------------------------
# Notifications
# ----------------------------------------------------------------------

@dataclass(slots=True)
class NotificationItem:
    """
    Notification displayed on dashboard.
    """

    level: str
    message: str

    title: str = ""
    timestamp: str = ""
    action: str = ""


# ----------------------------------------------------------------------
# Quick Actions
# ----------------------------------------------------------------------

@dataclass(slots=True)
class QuickAction:
    """
    Quick action shown on dashboard.
    """

    title: str
    route: str

    icon: str = ""
    tooltip: str = ""
    enabled: bool = True


# ----------------------------------------------------------------------
# Statistics
# ----------------------------------------------------------------------

@dataclass(slots=True)
class Statistic:
    """
    Generic statistic.

    Used later for graphs/charts.
    """

    key: str
    label: str
    value: float

    unit: str = ""


# ----------------------------------------------------------------------
# Dashboard Health
# ----------------------------------------------------------------------

@dataclass(slots=True)
class DashboardHealth:
    """
    Overall dashboard/application health.
    """

    status: str = "Healthy"

    database_connected: bool = True

    backup_available: bool = False

    validation_complete: bool = False

    last_backup: Optional[str] = None

    database_size: str = ""


# ----------------------------------------------------------------------
# Dashboard Data
# ----------------------------------------------------------------------

@dataclass(slots=True)
class DashboardData:
    """
    Complete dashboard model returned by DashboardService.
    """

    workspace: WorkspaceInfo = field(default_factory=WorkspaceInfo)

    summary_cards: List[SummaryCard] = field(default_factory=list)

    validation: ValidationSummary = field(default_factory=ValidationSummary)

    recent_activity: List[ActivityItem] = field(default_factory=list)

    notifications: List[NotificationItem] = field(default_factory=list)

    quick_actions: List[QuickAction] = field(default_factory=list)

    statistics: List[Statistic] = field(default_factory=list)

    health: DashboardHealth = field(default_factory=DashboardHealth)