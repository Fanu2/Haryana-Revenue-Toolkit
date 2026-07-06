"""
Haryana Revenue Toolkit (HRTK)

Khewat–Parcel Relationship Workspace.
"""

from __future__ import annotations

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSplitter,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.presentation.khewat_parcel.khewat_parcel_toolbar import (
    KhewatParcelToolbar,
)

from hrtk.presentation.khewat_parcel.parcel_selection_table import (
    ParcelSelectionTable,
)


class KhewatParcelWidget(QWidget):
    """
    Workspace for managing
    Khewat–Parcel relationships.
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
    # Widget Creation
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self.toolbar = (
            KhewatParcelToolbar()
        )

        #
        # Selection
        #

        self.village_combo = QComboBox()

        self.jamabandi_combo = QComboBox()

        self.khewat_combo = QComboBox()

        #
        # Tables
        #

        self.available_table = (
            ParcelSelectionTable()
        )

        self.assigned_table = (
            ParcelSelectionTable()
        )

        #
        # Buttons
        #

        self.assign_button = QPushButton(
            "► Assign",
        )

        self.remove_button = QPushButton(
            "◄ Remove",
        )

        #
        # Remarks
        #

        self.remarks_edit = QTextEdit()

        self.remarks_edit.setMaximumHeight(
            80,
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:

        layout = QVBoxLayout(self)

        layout.addWidget(
            self.toolbar,
        )

        #
        # Selection Group
        #

        selection_group = QGroupBox(
            "Selection",
        )

        selection_layout = QHBoxLayout()

        selection_layout.addWidget(
            QLabel("Village"),
        )

        selection_layout.addWidget(
            self.village_combo,
        )

        selection_layout.addWidget(
            QLabel("Jamabandi"),
        )

        selection_layout.addWidget(
            self.jamabandi_combo,
        )

        selection_layout.addWidget(
            QLabel("Khewat"),
        )

        selection_layout.addWidget(
            self.khewat_combo,
        )

        selection_group.setLayout(
            selection_layout,
        )

        layout.addWidget(
            selection_group,
        )

        #
        # Parcel Area
        #

        splitter = QSplitter(
            Qt.Horizontal,
        )

        splitter.addWidget(
            self.available_table,
        )

        buttons = QWidget()

        button_layout = QVBoxLayout(
            buttons,
        )

        button_layout.addStretch()

        button_layout.addWidget(
            self.assign_button,
        )

        button_layout.addWidget(
            self.remove_button,
        )

        button_layout.addStretch()

        splitter.addWidget(
            buttons,
        )

        splitter.addWidget(
            self.assigned_table,
        )

        splitter.setStretchFactor(
            0,
            1,
        )

        splitter.setStretchFactor(
            2,
            1,
        )

        layout.addWidget(
            splitter,
        )

        #
        # Remarks
        #

        remarks_group = QGroupBox(
            "Remarks",
        )

        remarks_layout = QVBoxLayout()

        remarks_layout.addWidget(
            self.remarks_edit,
        )

        remarks_group.setLayout(
            remarks_layout,
        )

        layout.addWidget(
            remarks_group,
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(
        self,
    ) -> None:

        self.toolbar.refresh_requested.connect(
            self.refresh,
        )

        self.assign_button.clicked.connect(
            self.assign_parcel,
        )

        self.remove_button.clicked.connect(
            self.remove_parcel,
        )

        self.village_combo.currentIndexChanged.connect(
            lambda: self._load_khewats(),
        )

        self.khewat_combo.currentIndexChanged.connect(
            self.refresh,
        )

    # ---------------------------------------------------------
    # Refresh
    # ---------------------------------------------------------

    def refresh(
        self,
    ) -> None:
        """
        Refresh parcel tables.
        """

        self._load_available_parcels()

        self._load_assigned_parcels()

    # ---------------------------------------------------------
    # Loading
    # ---------------------------------------------------------

    def _load_villages(
        self,
    ) -> None:
        """
        Load all villages.
        """

        self.village_combo.blockSignals(True)

        self.village_combo.clear()

        villages = (
            self._context
            .village_service
            .all()
        )

        for village in villages:

            self.village_combo.addItem(
                village.name,
                village.id,
            )

        self.village_combo.blockSignals(False)

        if self.village_combo.count():

            self._load_jamabandis()

    def _load_jamabandis(
        self,
    ) -> None:
        """
        Load all Jamabandis.
        """

        self.jamabandi_combo.blockSignals(True)

        self.jamabandi_combo.clear()

        jamabandis = (
            self._context
            .jamabandi_service
            .all()
        )

        for jamabandi in jamabandis:

            self.jamabandi_combo.addItem(
                jamabandi.year,
                jamabandi.id,
            )

        self.jamabandi_combo.blockSignals(False)

        if self.jamabandi_combo.count():

            self._load_khewats()

    def _load_khewats(
        self,
    ) -> None:

        from uuid import UUID

        self.khewat_combo.blockSignals(True)

        self.khewat_combo.clear()

        village_id = (
            self.village_combo.currentData()
        )

        if village_id is None:

            self.khewat_combo.blockSignals(False)

            return

        village_id = UUID(
            str(village_id),
        )

        khewats = (
            self._context
            .khewat_service
            .find_by_village(
                village_id,
            )
        )

        for khewat in khewats:

            self.khewat_combo.addItem(
                khewat.display_name,
                khewat.id,
            )

        self.khewat_combo.blockSignals(False)

        self.refresh()

    def _load_available_parcels(
        self,
    ) -> None:

        from uuid import UUID

        khewat_id = self.khewat_combo.currentData()

        if khewat_id is None:

            self.available_table.model.set_parcels([])

            return

        khewat_id = UUID(
            str(khewat_id),
        )

        parcels = (
            self._context
            .parcel_service
            .all()
        )

        relationships = (
            self._context
            .khewat_parcel_service
            .find_by_khewat(
                khewat_id,
            )
        )

        assigned_ids = {
            r.parcel_id
            for r in relationships
        }

        available = [
            parcel
            for parcel in parcels
            if parcel.id not in assigned_ids
        ]

        self.available_table.model.set_parcels(
            available,
        )

    def _load_assigned_parcels(
        self,
    ) -> None:

        from uuid import UUID

        khewat_id = self.khewat_combo.currentData()

        if khewat_id is None:

            self.assigned_table.model.set_parcels([])

            return

        khewat_id = UUID(
            str(khewat_id),
        )

        relationships = (
            self._context
            .khewat_parcel_service
            .find_by_khewat(
                khewat_id,
            )
        )

        parcel_lookup = {
            parcel.id: parcel
            for parcel in
            self._context
            .parcel_service
            .all()
        }

        assigned = []

        for relationship in relationships:

            parcel = parcel_lookup.get(
                relationship.parcel_id,
            )

            if parcel is not None:

                assigned.append(
                    parcel,
                )

        self.assigned_table.model.set_parcels(
            assigned,
        )

    # ---------------------------------------------------------
    # Relationship Operations
    # ---------------------------------------------------------

    def assign_parcel(
        self,
    ) -> None:
        """
        Assign the selected parcel to the selected
        Khewat.
        """

        from uuid import UUID, uuid4

        from hrtk.domain.land_records.khewat_parcel import (
            KhewatParcel,
        )

        parcel = (
            self.available_table.selected_parcel()
        )

        if parcel is None:
            return

        khewat_id = (
            self.khewat_combo.currentData()
        )

        if khewat_id is None:
            return

        khewat_id = UUID(
            str(khewat_id),
        )

        if (
            self._context
            .khewat_parcel_service
            .exists(
                khewat_id,
                parcel.id,
            )
        ):
            return

        relationship = KhewatParcel(
            id=uuid4(),
            khewat_id=khewat_id,
            parcel_id=parcel.id,
            remarks=self.remarks_edit.toPlainText(),
        )

        self._context.khewat_parcel_service.register(
            relationship,
        )

        self.refresh()

    def remove_parcel(
        self,
    ) -> None:
        """
        Remove parcel from the selected
        Khewat.
        """

        from uuid import UUID

        parcel = (
            self.assigned_table.selected_parcel()
        )

        if parcel is None:
            return

        khewat_id = (
            self.khewat_combo.currentData()
        )

        if khewat_id is None:
            return

        khewat_id = UUID(
            str(khewat_id),
        )

        relationships = (
            self._context
            .khewat_parcel_service
            .find_by_khewat(
                khewat_id,
            )
        )

        for relationship in relationships:

            if (
                relationship.parcel_id
                == parcel.id
            ):

                self._context\
                    .khewat_parcel_service\
                    .remove(
                        relationship.id,
                    )

                break

        self.refresh()
        