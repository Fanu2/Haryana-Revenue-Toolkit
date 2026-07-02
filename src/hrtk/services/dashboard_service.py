"""
Haryana Revenue Toolkit (HRTK)

Dashboard Service.

Aggregates information from application services for the
Dashboard module.

The dashboard must never access repositories directly.
"""

from __future__ import annotations

from typing import Any

from hrtk.services.dashboard_models import (
    ActivityItem,
    DashboardData,
    DashboardHealth,
    NotificationItem,
    QuickAction,
    Statistic,
    SummaryCard,
    ValidationSummary,
    WorkspaceInfo,
)


class DashboardService:
    """
    Aggregate application information for the Dashboard.

    This service has no knowledge of Qt widgets and no direct
    dependency on repositories.

    It simply coordinates existing application services.
    """

    def __init__(
        self,
        *,
        village_service: Any | None = None,
        owner_service: Any | None = None,
        khewat_service: Any | None = None,
        parcel_service: Any | None = None,
        ownership_service: Any | None = None,
        validation_service: Any | None = None,
        history_service: Any | None = None,
        app_context: Any | None = None,
    ) -> None:

        self._village_service = village_service
        self._owner_service = owner_service
        self._khewat_service = khewat_service
        self._parcel_service = parcel_service
        self._ownership_service = ownership_service
        self._validation_service = validation_service
        self._history_service = history_service
        self._app_context = app_context

    # ---------------------------------------------------------
    # public API
    # ---------------------------------------------------------

    def load(self) -> DashboardData:
        """
        Return the complete dashboard model.
        """

        return DashboardData(
            workspace=self.get_workspace(),
            summary_cards=self.get_summary_cards(),
            validation=self.get_validation_summary(),
            recent_activity=self.get_recent_activity(),
            notifications=self.get_notifications(),
            quick_actions=self.get_quick_actions(),
            statistics=self.get_statistics(),
            health=self.get_health(),
        )

    # ---------------------------------------------------------
    # workspace
    # ---------------------------------------------------------

    def get_workspace(self) -> WorkspaceInfo:

        if self._app_context is None:
            return WorkspaceInfo()

        return WorkspaceInfo(
            village=getattr(
                self._app_context,
                "active_village",
                "",
            ),
            jamabandi_year=getattr(
                self._app_context,
                "active_jamabandi",
                "",
            ),
            district=getattr(
                self._app_context,
                "district",
                "",
            ),
            tehsil=getattr(
                self._app_context,
                "tehsil",
                "",
            ),
            office=getattr(
                self._app_context,
                "office",
                "",
            ),
            database=getattr(
                self._app_context,
                "database_name",
                "",
            ),
            user=getattr(
                self._app_context,
                "current_user",
                "",
            ),
            workspace_name=getattr(
                self._app_context,
                "workspace_name",
                "",
            ),
        )

    # ---------------------------------------------------------
    # summary cards
    # ---------------------------------------------------------

    def get_summary_cards(self) -> list[SummaryCard]:

        return [

            SummaryCard(
                key="villages",
                title="Villages",
                value=self._entity_count(
                    self._village_service,
                ),
                icon="village",
                route="village",
            ),

            SummaryCard(
                key="owners",
                title="Owners",
                value=self._entity_count(
                    self._owner_service,
                ),
                icon="owner",
                route="owner",
            ),

            SummaryCard(
                key="khewats",
                title="Khewats",
                value=self._entity_count(
                    self._khewat_service,
                ),
                icon="khewat",
                route="khewat",
            ),

            SummaryCard(
                key="parcels",
                title="Parcels",
                value=self._entity_count(
                    self._parcel_service,
                ),
                icon="parcel",
                route="parcel",
            ),

            SummaryCard(
                key="ownerships",
                title="Ownerships",
                value=self._entity_count(
                    self._ownership_service,
                ),
                icon="ownership",
                route="ownership",
            ),
        ]

    # ---------------------------------------------------------
    # validation
    # ---------------------------------------------------------

    def get_validation_summary(self) -> ValidationSummary:

        if (
            self._validation_service is not None
            and hasattr(
                self._validation_service,
                "dashboard_summary",
            )
        ):
            return self._validation_service.dashboard_summary()

        return ValidationSummary(
            healthy=0,
            warnings=0,
            errors=0,
            message="Validation not yet available.",
        )

    # ---------------------------------------------------------
    # activity
    # ---------------------------------------------------------

    def get_recent_activity(
        self,
    ) -> list[ActivityItem]:

        if (
            self._history_service is not None
            and hasattr(
                self._history_service,
                "recent",
            )
        ):
            return self._history_service.recent()

        return []

    # ---------------------------------------------------------
    # notifications
    # ---------------------------------------------------------

    def get_notifications(
        self,
    ) -> list[NotificationItem]:

        return [

            NotificationItem(
                level="info",
                title="Welcome",
                message=(
                    "Welcome to Haryana Revenue Toolkit."
                ),
            )

        ]

    # ---------------------------------------------------------
    # quick actions
    # ---------------------------------------------------------

    def get_quick_actions(
        self,
    ) -> list[QuickAction]:

        return [

            QuickAction(
                title="Village",
                route="village",
                icon="village",
            ),

            QuickAction(
                title="Owner",
                route="owner",
                icon="owner",
            ),

            QuickAction(
                title="Khewat",
                route="khewat",
                icon="khewat",
            ),

            QuickAction(
                title="Parcel",
                route="parcel",
                icon="parcel",
            ),

            QuickAction(
                title="Reports",
                route="reports",
                icon="reports",
            ),

        ]

    # ---------------------------------------------------------
    # statistics
    # ---------------------------------------------------------

    def get_statistics(
        self,
    ) -> list[Statistic]:

        return []

    # ---------------------------------------------------------
    # health
    # ---------------------------------------------------------

    def get_health(
        self,
    ) -> DashboardHealth:

        return DashboardHealth(
            status="Healthy",
            database_connected=True,
            backup_available=False,
            validation_complete=False,
        )

    # ---------------------------------------------------------
    # helpers
    # ---------------------------------------------------------

    @staticmethod
    def _entity_count(
        service: Any | None,
    ) -> int:

        if service is None:
            return 0

        if hasattr(
            service,
            "count",
        ):
            try:
                return service.count()
            except Exception:
                pass

        if hasattr(
            service,
            "all",
        ):
            try:
                return len(service.all())
            except Exception:
                pass

        if hasattr(
            service,
            "list",
        ):
            try:
                return len(service.list())
            except Exception:
                pass

        return 0