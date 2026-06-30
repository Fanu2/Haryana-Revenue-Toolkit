"""
Haryana Revenue Toolkit (HRTK)

Owner Table.
"""

from __future__ import annotations

# ==========================================================
# Qt
# ==========================================================

from PySide6.QtCore import Signal

# ==========================================================
# HRTK
# ==========================================================

from hrtk.domain.owner import Owner
from hrtk.presentation.common.base_table import BaseTable
from hrtk.presentation.owner.owner_model import OwnerModel


class OwnerTable(BaseTable):
    """
    Table view for Owner entities.
    """

    owner_activated = Signal(Owner)

    def __init__(
        self,
        model: OwnerModel,
    ) -> None:
        super().__init__()

        self.setModel(model)

        self.clicked.connect(
            self._on_clicked,
        )

    @property
    def owner_model(self) -> OwnerModel:
        """
        Return the source owner model.
        """

        model = self.source_model()

        assert isinstance(
            model,
            OwnerModel,
        )

        return model

    def selected_owner(
        self,
    ) -> Owner | None:
        """
        Return the selected owner.
        """

        row = self.selected_source_row()

        if row is None:
            return None

        return self.owner_model.owner(
            row,
        )

    def _on_clicked(
        self,
        index,
    ) -> None:
        """
        Handle row selection.
        """

        source_index = self.map_to_source(
            index,
        )

        owner = self.owner_model.owner(
            source_index.row(),
        )

        if owner is not None:

            self.owner_activated.emit(
                owner,
            )