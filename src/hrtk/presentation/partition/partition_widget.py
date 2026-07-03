"""
Haryana Revenue Toolkit (HRTK)

Partition Workbench.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

from PySide6.QtCore import Qt

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.presentation.partition.partition_toolbar import (
    PartitionToolbar,
)

from hrtk.presentation.partition.partition_owner_table import (
    PartitionOwnerTable,
)

from hrtk.presentation.partition.partition_khasra_table import (
    PartitionKhasraTable,
)

from hrtk.presentation.partition.summary_panel import (
    SummaryPanel,
)

from hrtk.presentation.partition.validation_panel import (
    ValidationPanel,
)

from hrtk.presentation.partition.allocation_panel import (
    AllocationPanel,
)

from hrtk.presentation.partition.allocation_table import (
    AllocationTable,
)

from hrtk.presentation.partition.allocation_summary import (
    AllocationSummary,
)

from hrtk.presentation.partition.allocation_validation import (
    AllocationValidation,
)


class PartitionWidget(QWidget):
    """
    Main Partition Workbench.
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

        self._village_combo = QComboBox()

        self._jamabandi_combo = QComboBox()

        self._khewat_combo = QComboBox()

        self._toolbar = PartitionToolbar()

        self._owner_table = PartitionOwnerTable()

        self._khasra_table = PartitionKhasraTable()

        self._summary = SummaryPanel()

        self._validation = ValidationPanel()

        self._status = QLabel(
            "Ready"
        )

        
    #
    # Allocation
    #

        self._allocation_panel = (
            AllocationPanel()
        )

        self._allocation_table = (
            AllocationTable()
        )

        self._allocation_summary = (
            AllocationSummary()
        )

        self._allocation_validation = (
            AllocationValidation()
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:

        #
        # Top Selection Row
        #

        selector_layout = QHBoxLayout()

        selector_layout.addWidget(
            QLabel("Village")
        )

        selector_layout.addWidget(
            self._village_combo
        )

        selector_layout.addWidget(
            QLabel("Jamabandi")
        )

        selector_layout.addWidget(
            self._jamabandi_combo
        )

        selector_layout.addWidget(
            QLabel("Khewat")
        )

        selector_layout.addWidget(
            self._khewat_combo
        )

        selector_layout.addStretch()

    #
    # Main Work Area
    #

        splitter = QSplitter(
            Qt.Horizontal
        )

    #
    # Left : Owners
    #

        splitter.addWidget(
            self._owner_table
        )

    #
    # Centre : Khasras
    #

        splitter.addWidget(
            self._khasra_table
        )

    #
    # Right : Allocation Panel
    #

        splitter.addWidget(
            self._allocation_panel
        )

        splitter.setStretchFactor(
            0,
            2,
        )

        splitter.setStretchFactor(
            1,
            2,
        )

        splitter.setStretchFactor(
        2,
        1,
        )

    #
    # Allocation Register
    #

        allocation_group = QGroupBox(
            "Allocation Register"
        )

        allocation_layout = QVBoxLayout()

        allocation_layout.addWidget(
            self._allocation_table
        )

        allocation_group.setLayout(
            allocation_layout
        )

    #
    # Bottom Panels
    #

        bottom_layout = QHBoxLayout()

        bottom_layout.addWidget(
            self._summary
        )

        bottom_layout.addWidget(
            self._validation
        )

        bottom_layout.addWidget(
            self._allocation_summary
        )

        bottom_layout.addWidget(
        self._allocation_validation
        )

    #
    # Main Layout
    #

        layout = QVBoxLayout()

        layout.addWidget(
            self._toolbar
        )

        layout.addLayout(
            selector_layout
        )

        layout.addWidget(
            splitter
        )

        layout.addWidget(
            allocation_group
        )

        layout.addLayout(
            bottom_layout
        )

        layout.addWidget(
            self._status
        )

        self.setLayout(
            layout
        )

    #
    # Initial State
    #

        self._allocation_summary.clear()

        self._allocation_validation.show_default_state()
    
    
    def _connect_signals(
        self,
    ) -> None:

        self._village_combo.currentIndexChanged.connect(
            self._load_khewats,
        )

        self._khewat_combo.currentIndexChanged.connect(
            self._load_partition_data,
        )


        self._allocation_panel.allocate_requested.connect(
            self._allocate,
        )

    #
    # Owner Selection
    #

        self._owner_table.selectionModel().selectionChanged.connect(
            self._owner_selected,
        )

    #
    # Khasra Selection
    #

        self._khasra_table.selectionModel().selectionChanged.connect(
            self._khasra_selected,
        )

    #
    # Allocate
    #

        self._allocation_panel.allocate_requested.connect(
            self._allocate,
        )

    # ---------------------------------------------------------
    # Loading
    # ---------------------------------------------------------

    def _load_villages(
        self,
    ) -> None:
        """
        Load all villages.
        """

        self._village_combo.blockSignals(
            True,
        )

        self._village_combo.clear()

        villages = (
            self._context.village_service.all()
        )

        for village in villages:

            self._village_combo.addItem(
                village.name,
                village.id,
            )

        self._village_combo.blockSignals(
            False,
        )

        #
        # Temporary Jamabandi values
        #

        self._jamabandi_combo.clear()

        self._jamabandi_combo.addItems(
            [
                "2023-24",
                "2020-21",
                "2017-18",
                "2014-15",
            ]
        )

        if self._village_combo.count():

            self._load_khewats()

    def _load_khewats(
        self,
    ) -> None:
        """
        Load Khewats for the selected village.
        """

        self._khewat_combo.blockSignals(
            True,
        )

        self._khewat_combo.clear()

        village_id = (
            self._village_combo.currentData()
        )

        if village_id is None:

            self._khewat_combo.blockSignals(
                False,
            )

            return

        for khewat in (
            self._context.khewat_service.all()
        ):

            if khewat.village_id != village_id:
                continue

            self._khewat_combo.addItem(
                khewat.display_name,
                khewat.id,
            )

        self._khewat_combo.blockSignals(
            False,
        )

        if self._khewat_combo.count():

            self._load_partition_data()

    # ---------------------------------------------------------
    # Partition Workbench
    # ---------------------------------------------------------

    def _load_partition_data(
        self,
    ) -> None:
        """
        Load all information required by the
        Partition Workbench.
        """

        khewat_id = (
            self._khewat_combo.currentData()
        )

        if khewat_id is None:

            self._status.setText(
                "No Khewat selected."
            )

            return

    # ---------------------------------------------------------
    # Load Ownership Records
    # ---------------------------------------------------------

        ownerships = (
            self._context
            .ownership_service
            .by_khewat(
                khewat_id,
            )
        )

    # ---------------------------------------------------------
    # Load Parcels (Temporary)
    #
    # Stable Parcel module does not yet support
    # Khewat filtering, so load all parcels.
    # ---------------------------------------------------------

        khasras = []

        if hasattr(
            self._context,
            "parcel_service",
        ):

            khasras = (
            self._context
            .parcel_service
            .list()
        )
            
        print("PARCEL COUNT =", len(khasras))
        for p in khasras:
            print(p)

    # ---------------------------------------------------------
    # Owner Lookup
    # ---------------------------------------------------------

        owner_names = {}

        for owner in (
            self._context.owner_service.all()
        ):

            owner_names[
                str(owner.id)
            ] = owner.display_name

    # ---------------------------------------------------------
    # Populate Owner Table
    # ---------------------------------------------------------

        if hasattr(
            self._owner_table,
            "set_ownerships",
        ):

            self._owner_table.set_ownerships(
                ownerships,
                owner_names,
            )

    # ---------------------------------------------------------
    # Populate Khasra Table
    # ---------------------------------------------------------

        if hasattr(
            self._khasra_table,
            "set_khasras",
        ):

            self._khasra_table.set_khasras(
            khasras,
            )

        print(
            "ROWS =",
            self._khasra_table.model.rowCount(),
        )

    # ---------------------------------------------------------
    # Summary Panel
    # ---------------------------------------------------------

        if hasattr(
            self._summary,
            "update_summary",
        ):

            self._summary.update_summary(
                ownerships,
                khasras,
        )

    # ---------------------------------------------------------
    # Validation Panel
    # ---------------------------------------------------------

        if hasattr(
            self._validation,
            "clear",
        ):

            self._validation.clear()

    # ---------------------------------------------------------
    # Status
    # ---------------------------------------------------------

        self._status.setText(
            f"Loaded {len(ownerships)} Owners, "
            f"{len(khasras)} Khasras."
        )

    def _allocate(
        self,
    ) -> None:
        """
        Temporary allocation placeholder.
        """

        self._status.setText(
            "Allocation Engine coming next."
        )

    def _owner_selected(
        self,
    ) -> None:
        """
        Ownership selection changed.
        """

        ownership = (
            self._owner_table.selected_ownership()
        )

        if ownership is None:

            self._allocation_panel.set_owner(
                "---"
            )

            return

        owner = (
            self._context.owner_service.get(
                ownership.owner_id,
            )
        )

        if owner is None:

            self._allocation_panel.set_owner(
                "Unknown Owner"
            )

            return

        self._allocation_panel.set_owner(
            owner.display_name
        )

        self._status.setText(
            f"Owner selected: {owner.display_name}"
        )

    def _khasra_selected(
        self,
    ) -> None:
        """
        Khasra selection changed.
        """

        parcel = (
            self._khasra_table.selected_khasra()
        )

        if parcel is None:

            self._allocation_panel.set_khasra(
                "---"
            )

            self._allocation_panel.set_remaining_area(
                "0K-0M-0S"
            )

            return

        self._allocation_panel.set_khasra(
            str(parcel.number)
        )

        self._allocation_panel.set_remaining_area(
            parcel.area.display()
        )

        self._status.setText(
            f"Khasra selected: {parcel.number}"
        )