"""
Haryana Revenue Toolkit (HRTK)

Ownership Workspace.
"""

from __future__ import annotations

from uuid import UUID, uuid4

from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.domain.ownership import Ownership

from hrtk.presentation.common.form_mode import (
    FormMode,
)

from hrtk.presentation.ownership.ownership_dialog import (
    OwnershipDialog,
)

from hrtk.presentation.ownership.ownership_table import (
    OwnershipTable,
)

from hrtk.presentation.ownership.ownership_toolbar import (
    OwnershipToolbar,
)

from hrtk.presentation.common.message_service import (
    MessageService,
)


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
    # Widget Creation
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self._village_combo = QComboBox(
            self,
        )

        self._khewat_combo = QComboBox(
            self,
        )

        self._toolbar = OwnershipToolbar()

        self._table = OwnershipTable()

        self._total_label = QLabel(
            "Ownership Records : 0",
            self,
        )

        self._status_label = QLabel(
            "Ready",
            self,
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
            self._load_khewats,
        )

        self._khewat_combo.currentIndexChanged.connect(
            self._load_ownerships,
        )

        self._toolbar.add_requested.connect(
            self._add_ownership,
        )

        self._toolbar.edit_requested.connect(
            self._edit_ownership,
        )

        self._toolbar.refresh_requested.connect(
            self._load_ownerships,
        )

        self._toolbar.delete_requested.connect(
        self._delete_ownership,
        )
        
        self._toolbar.validate_requested.connect(
        self._validate_ownership,
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

        if self._village_combo.count():

            self._load_khewats()

    def _load_khewats(
        self,
    ) -> None:
        """
        Load Khewats for selected village.
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

        village_id = UUID(
            str(village_id),
        )

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

            self._load_ownerships()

        else:

            self._table.model.set_ownerships(
                [],
                {},
            )

            self._total_label.setText(
                "Ownership Records : 0"
            )

            self._status_label.setText(
                "No Khewats found."
            )

    def _load_ownerships(
        self,
    ) -> None:
        """
        Load Ownership records.
        """

        khewat_id = (
            self._khewat_combo.currentData()
        )

        if khewat_id is None:

            self._table.model.set_ownerships(
                [],
                {},
            )

            return

        khewat_id = UUID(
            str(khewat_id),
        )

        ownerships = (
            self._context
            .ownership_service
            .by_khewat(
                khewat_id,
            )
        )

        owner_lookup = {}

        for owner in (
            self._context.owner_service.all()
        ):

            owner_lookup[
                str(owner.id)
            ] = owner.display_name

        self._table.model.set_ownerships(
            ownerships,
            owner_lookup,
        )

        self._total_label.setText(
            f"Ownership Records : {len(ownerships)}"
        )

        self._status_label.setText(
            "Loaded successfully."
        )
    # ---------------------------------------------------------
    # Add Ownership
    # ---------------------------------------------------------

    def _add_ownership(
        self,
    ) -> None:
        """
        Add a new ownership.
        """

        khewat_id = self._khewat_combo.currentData()

        if khewat_id is None:

            self._status_label.setText(
                "Please select a Khewat."
            )

            return

        khewat_id = UUID(
            str(khewat_id),
        )

        dialog = OwnershipDialog(
            FormMode.CREATE,
        )

        owners = []

        for owner in (
            self._context.owner_service.all()
        ):

            owners.append(
                (
                    str(owner.id),
                    owner.display_name,
                )
            )

        dialog.set_owners(
            owners,
        )

        if not dialog.exec():

            self._status_label.setText(
                "Operation cancelled."
            )

            return

        owner_id, share, remarks = (
            dialog.ownership_data()
        )

        owner_id = UUID(
            str(owner_id),
        )

        #
        # Prevent duplicate ownership
        #

        if (
            self._context
            .ownership_service
            .exists(
                owner_id,
                khewat_id,
            )
        ):

            self._status_label.setText(
                "Owner already exists in this Khewat."
            )

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

        self._status_label.setText(
            "Ownership created successfully."
        )
    # ---------------------------------------------------------
    # Edit Ownership
    # ---------------------------------------------------------

    def _edit_ownership(
        self,
    ) -> None:
        """
        Edit the selected ownership.
        """

        ownership = (
            self._table.selected_ownership()
        )

        if ownership is None:

            self._status_label.setText(
                "Please select an ownership."
            )

            return

        dialog = OwnershipDialog(
            FormMode.EDIT,
        )

        owners = []

        for owner in (
            self._context.owner_service.all()
        ):

            owners.append(
                (
                    str(owner.id),
                    owner.display_name,
                )
            )

        dialog.set_owners(
            owners,
        )

        dialog.set_ownership(
            ownership,
        )

        if not dialog.exec():

            self._status_label.setText(
                "Edit cancelled."
            )

            return

        dialog.update_ownership(
            ownership,
        )

        self._context.ownership_service.update(
            ownership,
        )

        self._load_ownerships()

        self._status_label.setText(
            "Ownership updated successfully."
        )

    # ---------------------------------------------------------
    # Future Delete Support
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # Delete Ownership
    # ---------------------------------------------------------

    def _delete_ownership(
        self,
    ) -> None:
        """
        Delete the selected ownership.
        """

        ownership = (
            self._table.selected_ownership()
        )

        if ownership is None:

            self._status_label.setText(
                "Please select an ownership."
            )

            return

        # ------------------------------------------
        # Confirmation
        # ------------------------------------------

        if not MessageService.confirm(
            self,
            "Delete Ownership",
            "Delete selected ownership?",
        ):
            return

        # ------------------------------------------
        # Delete
        # ------------------------------------------

        self._context.ownership_service.remove(
            ownership.id,
        )

        self._load_ownerships()

        self._status_label.setText(
            "Ownership deleted successfully."
        )

    # ---------------------------------------------------------
    # Validate Ownership
    # ---------------------------------------------------------

    def _validate_ownership(
        self,
    ) -> None:
        """
        Validate ownership records of the selected Khewat.
        """

        khewat_id = self._khewat_combo.currentData()

        if khewat_id is None:

            self._status_label.setText(
                "Please select a Khewat."
            )

            return

        ownerships = (
            self._context
            .ownership_service
            .by_khewat(
                UUID(str(khewat_id))
            )
        )

        #
        # Duplicate owners
        #

        owners = set()

        for ownership in ownerships:

            if ownership.owner_id in owners:

                MessageService.warning(
                    self,
                    "Validation",
                    "Duplicate owner found.",
                )

                self._status_label.setText(
                    "Validation failed."
                )

                return

            owners.add(
                ownership.owner_id
            )

        #
        # Total share
        #

        numerator = 0
        denominator = 1

        for ownership in ownerships:

            numerator = (
                numerator * ownership.share.denominator
                +
                ownership.share.numerator * denominator
            )

            denominator *= (
                ownership.share.denominator
            )

        #
        # Reduce fraction
        #

        from math import gcd

        g = gcd(
            numerator,
            denominator,
        )

        numerator //= g
        denominator //= g

        if (
            numerator == 1
            and denominator == 1
        ):

            MessageService.success(
                self,
                "Ownership validation successful.",
            )

            self._status_label.setText(
                "✔ Ownership Valid"
            )

        else:

            MessageService.warning(
                self,
                "Validation",
                f"Total Share = {numerator}/{denominator}"
            )

            self._status_label.setText(
                f"✖ Total = {numerator}/{denominator}"
            )