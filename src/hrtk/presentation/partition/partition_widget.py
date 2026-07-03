"""
Haryana Revenue Toolkit (HRTK)

Partition Workbench.
"""

from __future__ import annotations

from uuid import uuid4

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.domain.partition_allocation import (
    PartitionAllocation,
)

from hrtk.presentation.partition.allocation_panel import (
    AllocationPanel,
)

from hrtk.presentation.partition.allocation_summary import (
    AllocationSummary,
)

from hrtk.presentation.partition.allocation_validation import (
    AllocationValidation,
)

from hrtk.presentation.partition.partition_allocation_table import (
    PartitionAllocationTable,
)

from hrtk.presentation.partition.partition_khasra_table import (
    PartitionKhasraTable,
)

from hrtk.presentation.partition.partition_owner_table import (
    PartitionOwnerTable,
)

from hrtk.presentation.partition.partition_toolbar import (
    PartitionToolbar,
)

from hrtk.presentation.partition.summary_panel import (
    SummaryPanel,
)

from hrtk.presentation.partition.validation_panel import (
    ValidationPanel,
)


class PartitionWidget(
    QWidget,
):
    """
    Main Partition Workbench.

    Coordinates the user interface for
    partition proceedings while delegating
    business rules to the service layer.
    """

    def __init__(
        self,
        context: ApplicationContext,
        parent=None,
    ) -> None:

        super().__init__(parent)

        #
        # Context
        #

        self._context = context

        #
        # Runtime State
        #

        self._allocations: list[
            PartitionAllocation
        ] = []

        #
        # Build User Interface
        #

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

        #
        # Load Initial Data
        #

        self._load_villages()

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:
        """
        Create all widgets used by the
        Partition Workbench.
        """

        #
        # Selection
        #

        self._village_combo = QComboBox()

        self._jamabandi_combo = QComboBox()

        self._khewat_combo = QComboBox()

        #
        # Workbench
        #

        self._toolbar = (
            PartitionToolbar()
        )

        self._owner_table = (
            PartitionOwnerTable()
        )

        self._khasra_table = (
            PartitionKhasraTable()
        )

        self._allocation_panel = (
            AllocationPanel()
        )

        self._allocation_table = (
            PartitionAllocationTable()
        )

        #
        # Summary
        #

        self._summary = (
            SummaryPanel()
        )

        self._validation = (
            ValidationPanel()
        )

        self._allocation_summary = (
            AllocationSummary()
        )

        self._allocation_validation = (
            AllocationValidation()
        )

        #
        # Status
        #

        self._status = QLabel(
            "Ready"
        )

        #
        # Initial State
        #

        self._allocation_summary.clear()

        self._allocation_validation.show_default_state()

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:
        """
        Build the Partition Workbench layout.
        """

        #
        # Selection Bar
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
        # Main Workspace
        #

        splitter = QSplitter(
            Qt.Horizontal,
        )

        #
        # Owner Table
        #

        splitter.addWidget(
            self._owner_table,
        )

        #
        # Khasra Table
        #

        splitter.addWidget(
            self._khasra_table,
        )

        #
        # Allocation Panel
        #

        splitter.addWidget(
            self._allocation_panel,
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
            "Allocation Register",
        )

        allocation_layout = QVBoxLayout()

        allocation_layout.addWidget(
            self._allocation_table,
        )

        allocation_group.setLayout(
            allocation_layout,
        )

        #
        # Bottom Information Panels
        #

        bottom_layout = QHBoxLayout()

        bottom_layout.addWidget(
            self._summary,
        )

        bottom_layout.addWidget(
            self._validation,
        )

        bottom_layout.addWidget(
            self._allocation_summary,
        )

        bottom_layout.addWidget(
            self._allocation_validation,
        )

        #
        # Main Layout
        #

        layout = QVBoxLayout()

        layout.addWidget(
            self._toolbar,
        )

        layout.addLayout(
            selector_layout,
        )

        layout.addWidget(
            splitter,
        )

        layout.addWidget(
            allocation_group,
        )

        layout.addLayout(
            bottom_layout,
        )

        layout.addWidget(
            self._status,
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
        """
        Connect all widget signals.
        """

        #
        # Selection
        #

        self._village_combo.currentIndexChanged.connect(
            self._load_khewats,
        )

        self._khewat_combo.currentIndexChanged.connect(
            self._load_partition_data,
        )

        #
        # Workbench
        #

        self._owner_table.selectionModel().selectionChanged.connect(
            self._owner_selected,
        )

        self._khasra_table.selectionModel().selectionChanged.connect(
            self._khasra_selected,
        )

        #
        # Allocation
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
        Load available villages.
        """

        self._village_combo.blockSignals(
            True,
        )

        self._village_combo.clear()

        villages = (
            self._context
            .village_service
            .all()
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
        # Temporary Jamabandi Years
        #

        self._jamabandi_combo.clear()

        self._jamabandi_combo.addItems(
            (
                "2023-24",
                "2020-21",
                "2017-18",
                "2014-15",
            )
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
            self._context
            .khewat_service
            .all()
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

    def _load_partition_data(
        self,
    ) -> None:
        """
        Load the complete Partition Workbench.
        """

        khewat_id = (
            self._khewat_combo.currentData()
        )

        if khewat_id is None:

            self._status.setText(
                "No Khewat selected."
            )

            return

        #
        # Ownership
        #

        ownerships = (
            self._context
            .ownership_service
            .by_khewat(
                khewat_id,
            )
        )

        #
        # Parcels
        #
        # Stable Parcel module currently
        # returns all parcels.
        #

        khasras = (
            self._context
            .parcel_service
            .list()
        )

        #
        # Owner Lookup
        #

        owner_names: dict[
            str,
            str,
        ] = {}

        for owner in (
            self._context
            .owner_service
            .all()
        ):

            owner_names[
                str(owner.id)
            ] = owner.display_name

        #
        # Owner Table
        #

        self._owner_table.set_ownerships(
            ownerships,
            owner_names,
        )

        #
        # Khasra Table
        #

        self._khasra_table.set_khasras(
            khasras,
        )

        #
        # Summary
        #

        self._summary.update_summary(
            ownerships,
            khasras,
        )

        #
        # Validation
        #

        self._validation.clear()

        #
        # Status
        #

        self._status.setText(
            f"Loaded "
            f"{len(ownerships)} Owners, "
            f"{len(khasras)} Khasras."
        )

    # ---------------------------------------------------------
    # Selection
    # ---------------------------------------------------------

    def _owner_selected(
        self,
    ) -> None:
        """
        Handle Owner selection changes.
        """

        ownership = (
            self._owner_table.selected_ownership()
        )

        if ownership is None:

            self._allocation_panel.set_owner(
                "---",
            )

            self._status.setText(
                "No owner selected."
            )

            return

        owner_name = (
            self._owner_table.selected_owner_name()
        )

        self._allocation_panel.set_owner(
            owner_name,
        )

        self._status.setText(
            f"Owner selected: {owner_name}"
        )

    def _khasra_selected(
        self,
    ) -> None:
        """
        Handle Khasra selection changes.
        """

        parcel = (
            self._khasra_table.selected_khasra()
        )

        if parcel is None:

            self._allocation_panel.set_khasra(
                "---",
            )

            self._allocation_panel.set_remaining_area(
                "0K-0M-0S",
            )

            self._status.setText(
                "No Khasra selected."
            )

            return

        self._allocation_panel.set_khasra(
            str(
                parcel.number,
            ),
        )

        self._allocation_panel.set_remaining_area(
            parcel.area.display(),
        )

        self._status.setText(
            (
                "Khasra selected: "
                f"{parcel.number}"
            ),
        )

    # ---------------------------------------------------------
    # Allocation
    # ---------------------------------------------------------

    def _allocate(
        self,
    ) -> None:
        """
        Create an in-memory allocation from the
        currently selected Owner and Khasra.
        """

        ownership = (
            self._owner_table.selected_ownership()
        )

        if ownership is None:

            self._status.setText(
                "Select an owner."
            )

            return

        parcel = (
            self._khasra_table.selected_khasra()
        )

        if parcel is None:

            self._status.setText(
                "Select a Khasra."
            )

            return

        allocation = PartitionAllocation(
            id=uuid4(),
            partition_case_id=uuid4(),
            owner_id=ownership.owner_id,
            parcel_number=parcel.number,
            allocated_area=parcel.area,
            remarks="",
        )

        self._allocations.append(
            allocation,
        )

        self._refresh_allocation_register()

        self._status.setText(
            "Allocation created."
        )

    def _refresh_allocation_register(
        self,
    ) -> None:
        """
        Refresh the Allocation Register.
        """

        owner_names: dict[
            str,
            str,
        ] = {}

        for owner in (
            self._context
            .owner_service
            .all()
        ):

            owner_names[
                str(owner.id)
            ] = owner.display_name

        parcel_numbers: dict[
            str,
            str,
        ] = {}

        for parcel in (
            self._context
            .parcel_service
            .list()
        ):

            parcel_numbers[
                str(parcel.number)
            ] = str(
                parcel.number
            )

        self._allocation_table.set_allocations(
            self._allocations,
            owner_names,
            parcel_numbers,
        )

        self._allocation_table.refresh()