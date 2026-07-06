"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Workspace.
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

from hrtk.presentation.jamabandi.jamabandi_toolbar import (
    JamabandiToolbar,
)

from hrtk.presentation.jamabandi.jamabandi_table import (
    JamabandiTable,
)


class JamabandiWidget(QWidget):
    """
    Workspace for managing
    Jamabandi records.
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

        self.refresh()

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        #
        # Toolbar
        #

        self.toolbar = (
            JamabandiToolbar()
        )

        #
        # Selection
        #

        self.village_combo = QComboBox()

        self.year_combo = QComboBox()

        self.khewat_combo = QComboBox()

        #
        # Table
        #

        self.table = (
            JamabandiTable()
        )

        #
        # Buttons
        #

        self.add_button = QPushButton(
            "Add",
        )

        self.edit_button = QPushButton(
            "Edit",
        )

        self.delete_button = QPushButton(
            "Delete",
        )

        self.refresh_button = QPushButton(
            "Refresh",
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

        #
        # Toolbar
        #

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

        #
        # Village
        #

        selection_layout.addWidget(
            QLabel("Village"),
        )

        selection_layout.addWidget(
            self.village_combo,
        )

        #
        # Jamabandi Year
        #

        selection_layout.addWidget(
            QLabel("Year"),
        )

        selection_layout.addWidget(
            self.year_combo,
        )

        #
        # Khewat
        #

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
        # Jamabandi Records
        #

        splitter = QSplitter(
            Qt.Vertical,
        )

        splitter.addWidget(
            self.table,
        )

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

        splitter.addWidget(
            remarks_group,
        )

        splitter.setStretchFactor(
            0,
            5,
        )

        splitter.setStretchFactor(
            1,
            1,
        )

        layout.addWidget(
            splitter,
        )

        #
        # Action Buttons
        #

        button_layout = QHBoxLayout()

        button_layout.addStretch()

        button_layout.addWidget(
            self.add_button,
        )

        button_layout.addWidget(
            self.edit_button,
        )

        button_layout.addWidget(
            self.delete_button,
        )

        button_layout.addWidget(
            self.refresh_button,
        )

        layout.addLayout(
            button_layout,
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(
        self,
    ) -> None:

        #
        # Toolbar
        #

        self.toolbar.refresh_requested.connect(
            self.refresh,
        )

        #
        # Buttons
        #

        self.add_button.clicked.connect(
            self.add_jamabandi,
        )

        self.edit_button.clicked.connect(
            self.edit_jamabandi,
        )

        self.delete_button.clicked.connect(
            self.delete_jamabandi,
        )

        self.refresh_button.clicked.connect(
            self.refresh,
        )

        #
        # Selection
        #

        self.village_combo.currentIndexChanged.connect(
            lambda: self._load_khewats(),
        )

        self.year_combo.currentIndexChanged.connect(
            self.refresh,
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
        Refresh the workspace.
        """

        self._load_villages()

        self._load_jamabandis()

        self._load_khewats()

        self._load_table()

    # ---------------------------------------------------------
    # Loading
    # ---------------------------------------------------------

    def _load_villages(
        self,
    ) -> None:
        """
        Load villages.
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

    def _load_jamabandis(
        self,
    ) -> None:
        """
        Load Jamabandi years.
        """

        self.year_combo.blockSignals(True)

        self.year_combo.clear()

        jamabandis = (
            self._context
            .jamabandi_service
            .list()
        )

        years = sorted(
            {
                jamabandi.year
                for jamabandi in jamabandis
            }
        )

        for year in years:

            self.year_combo.addItem(
                year,
            )

        self.year_combo.blockSignals(False)

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

    def _load_table(
        self,
    ) -> None:
        """
        Load Jamabandi records into the table.
        """

        records = (
            self._context
            .jamabandi_service
            .list()
        )

        year = (
            self.year_combo.currentText()
        )

        if year:

            records = [
                record
                for record in records
                if record.year == year
            ]

        self.table.model.set_records(
            records,
        )
    # ---------------------------------------------------------
    # CRUD Operations
    # ---------------------------------------------------------

    def add_jamabandi(
        self,
    ) -> None:
        """
        Open Add Jamabandi dialog.
        """

        from hrtk.presentation.jamabandi.jamabandi_dialog import (
            JamabandiDialog,
        )

        dialog = JamabandiDialog(
            context=self._context,
            parent=self,
        )

        if dialog.exec():

            self.refresh()

    def edit_jamabandi(
        self,
    ) -> None:
        """
        Edit the selected Jamabandi.
        """

        record = self.table.selected_jamabandi()

        if record is None:
            return

        from hrtk.presentation.jamabandi.jamabandi_dialog import (
            JamabandiDialog,
        )

        dialog = JamabandiDialog(
            context=self._context,
            jamabandi=record,
            parent=self,
        )

        if dialog.exec():

            self.refresh()

    def delete_jamabandi(
        self,
    ) -> None:
        """
        Delete the selected Jamabandi.
        """

        record = self.table.selected_jamabandi()

        if record is None:
            return

        self._context\
            .jamabandi_service\
            .remove(
                record.id,
            )

        self.refresh()