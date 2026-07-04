"""
Haryana Revenue Toolkit (HRTK)

Jamabandi domain entity.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from hrtk.domain.base_entity import BaseEntity


@dataclass(
    slots=True,
)
class Jamabandi(BaseEntity):
    """
    Represents one Jamabandi
    (Record of Rights).

    A Jamabandi belongs to one
    Village and one Settlement Year.

    Khewats, Ownerships and Parcels
    are linked to a Jamabandi.
    """

    village_id: UUID

    year: str

    mutation_no: str = ""

    remarks: str = ""

    finalized: bool = False

    active: bool = True

    # ---------------------------------------------------------
    # Status
    # ---------------------------------------------------------

    def activate(
        self,
    ) -> None:
        """
        Mark the Jamabandi active.
        """

        self.active = True

    def deactivate(
        self,
    ) -> None:
        """
        Mark the Jamabandi inactive.
        """

        self.active = False

    # ---------------------------------------------------------
    # Finalization
    # ---------------------------------------------------------

    def finalize(
        self,
    ) -> None:
        """
        Mark the Jamabandi finalized.
        """

        self.finalized = True

    def reopen(
        self,
    ) -> None:
        """
        Re-open a finalized Jamabandi.
        """

        self.finalized = False

    # ---------------------------------------------------------
    # Display
    # ---------------------------------------------------------

    @property
    def display_name(
        self,
    ) -> str:
        """
        Display text.
        """

        return self.year

    def __str__(
        self,
    ) -> str:

        return (
            f"Jamabandi {self.year}"
        )
    
