"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Entity.
"""

from __future__ import annotations

from dataclasses import (
    dataclass,
    field,
)

from uuid import (
    UUID,
    uuid4,
)


@dataclass(
    slots=True,
    kw_only=True,
)
class Jamabandi:
    """
    Represents a Jamabandi record.

    A Jamabandi references an existing
    Village and Khewat.

    Owners and Parcels are assembled
    dynamically by the service layer.
    """

    # ---------------------------------------------------------
    # Identity
    # ---------------------------------------------------------

    id: UUID = field(
        default_factory=uuid4,
    )

    # ---------------------------------------------------------
    # References
    # ---------------------------------------------------------

    village_id: UUID

    khewat_id: UUID

    # ---------------------------------------------------------
    # Record
    # ---------------------------------------------------------

    year: str

    khatauni_number: str

    remarks: str = ""

    status: str = "Active"

    # ---------------------------------------------------------
    # Display
    # ---------------------------------------------------------

    def display(self) -> str:
        """
        Human-readable description.
        """

        return (
            f"Jamabandi "
            f"{self.year} "
            f"(Khewat {self.khewat_id})"
        )

    def __str__(self) -> str:

        return self.display()

    def __repr__(self) -> str:

        return (
            "Jamabandi("
            f"id={self.id}, "
            f"year={self.year}, "
            f"khewat_id={self.khewat_id}"
            ")"
        )