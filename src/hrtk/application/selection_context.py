"""
Haryana Revenue Toolkit (HRTK)

Selection Context.

Maintains the current application selection.
"""

from __future__ import annotations

from PySide6.QtCore import QObject, Signal

from hrtk.domain.owner import Owner
from hrtk.domain.village import Village


class SelectionContext(QObject):
    """
    Stores the current application selection.
    """

    village_changed = Signal(object)
    owner_changed = Signal(object)

    def __init__(self) -> None:
        super().__init__()

        self._village: Village | None = None
        self._owner: Owner | None = None

    # ---------------------------------------------------------
    # Village
    # ---------------------------------------------------------

    @property
    def village(self) -> Village | None:
        return self._village

    @village.setter
    def village(
        self,
        village: Village | None,
    ) -> None:

        if village is self._village:
            return

        self._village = village

        #
        # Clear dependent selection
        #
        self._owner = None

        self.village_changed.emit(village)

    # ---------------------------------------------------------
    # Owner
    # ---------------------------------------------------------

    @property
    def owner(self) -> Owner | None:
        return self._owner

    @owner.setter
    def owner(
        self,
        owner: Owner | None,
    ) -> None:

        if owner is self._owner:
            return

        self._owner = owner

        self.owner_changed.emit(owner)


    @property
    def has_village(self) -> bool:
        """
        Return True when a village is selected.
        """
        return self._village is not None


    @property
    def has_owner(self) -> bool:
        """
        Return True when an owner is selected.
        """
        return self._owner is not None

    # ---------------------------------------------------------
    # Utilities
    # ---------------------------------------------------------

    def clear(self) -> None:
        """
        Clear all selections.
        """

        self._village = None
        self._owner = None

        self.village_changed.emit(None)
        self.owner_changed.emit(None)