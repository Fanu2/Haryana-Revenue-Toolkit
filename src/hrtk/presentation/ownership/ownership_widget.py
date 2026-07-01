"""
Haryana Revenue Toolkit (HRTK)

Ownership Workspace.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.presentation.ownership.ownership_table import (
    OwnershipTable,
)

from hrtk.presentation.ownership.ownership_toolbar import (
    OwnershipToolbar,
)


from hrtk.presentation.ownership.ownership_dialog import (
    OwnershipDialog,
)

from hrtk.domain.ownership import Ownership

from uuid import UUID, uuid4


class OwnershipWidget(QWidget):
    """
    Ownership Workspace.
    """

    def __init__(
        self,
        context: ApplicationContext,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._context = context

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

        self._load_villages()

        

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self._village_combo = QComboBox()

        self._khewat_combo = QComboBox()

        self._toolbar = OwnershipToolbar()

        self._table = OwnershipTable()

        self._total_label = QLabel(
            "Total Share : 0/1"
        )

        self._status_label = QLabel(
            "Status : ---"
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:

        layout = QVBoxLayout()

        layout.addWidget(
            self._village_combo,
        )

        layout.addWidget(
            self._khewat_combo,
        )

        layout.addWidget(
            self._toolbar,
        )

        layout.addWidget(
            self._table,
        )

        layout.addWidget(
            self._total_label,
        )

        layout.addWidget(
            self._status_label,
        )

        self.setLayout(
            layout,
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(
        self,
    ) -> None:

        self._village_combo.currentIndexChanged.connect(
            self._load_khewats
        )

        self._khewat_combo.currentIndexChanged.connect(
            self._load_ownerships
        )

        self._toolbar.refresh_requested.connect(
            self._load_ownerships
        )

        self._toolbar.add_requested.connect(
            self._add_ownership
        )

    # ---------------------------------------------------------
    # Loading
    # ---------------------------------------------------------

    def _load_villages(
        self,
    ) -> None:

        self._village_combo.clear()

        villages = (
            self._context.village_service.all()
        )

        for village in villages:

            self._village_combo.addItem(
                village.name,
                village.id,
            )

    def _load_khewats(
        self,
    ) -> None:

        self._khewat_combo.clear()

        village_id = self._village_combo.currentData()

        if village_id is None:
            return

        khewats = self._context.khewat_service.all()

        for khewat in khewats:

            #
            # Filter by village
            #
            if khewat.village_id == village_id:

                self._khewat_combo.addItem(
                    khewat.display_name,
                    khewat.id,
            )

    def _load_ownerships(
        self,
    ) -> None:

        khewat_id = self._khewat_combo.currentData()

        if khewat_id is None:
            return

        ownerships = (
            self._context.ownership_service.by_khewat(
                khewat_id,
            )
        )

        #
        # Temporary owner lookup
        #
        owner_names = {}

        for owner in self._context.owner_service.all():

            owner_names[str(owner.id)] = owner.owner_name

        self._table.model.set_ownerships(
            ownerships,
            owner_names,
        )

        self._total_label.setText(
            f"Ownership Records : {len(ownerships)}"
        )

        self._status_label.setText(
            "Loaded"
        )

    def _add_ownership(
        self,
    ) -> None:

        dialog = OwnershipDialog(self)

        #
        # Load Owners
        #

        owners = []

        for owner in self._context.owner_service.all():

            owners.append(
                (
                    str(owner.id),
                    owner.owner_name,
                )
            )

        dialog.set_owners(
            owners,
        )

        if not dialog.exec():
            return

        owner_id, share, remarks = (
            dialog.ownership_data()
        )

        owner_id = UUID(owner_id)

        khewat_id = (
            self._khewat_combo.currentData()
        )

        if khewat_id is None:
            return

        ownership = Ownership(
            id=uuid4(),
            owner_id=owner_id,
            khewat_id=khewat_id,
            share=share,
            remarks=remarks,
        )

        self._context.ownership_service.register(
            ownership,
        )

        self._load_ownerships()