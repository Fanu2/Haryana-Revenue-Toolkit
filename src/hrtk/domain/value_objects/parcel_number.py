"""
Haryana Revenue Toolkit (HRTK)

Parcel Number Value Object.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class ParcelNumber:
    """
    Immutable parcel number.

    Represents a Haryana parcel
    as Rectangle + Killa.
    """

    rectangle: int

    killa: str

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def __post_init__(self) -> None:
        """
        Validate the parcel number.
        """

        if self.rectangle <= 0:
            raise ValueError(
                "Rectangle number must be greater than zero."
            )

        if not self.killa:
            raise ValueError(
                "Killa number cannot be empty."
            )

        if " " in self.killa:
            raise ValueError(
                "Killa number cannot contain spaces."
            )

        if self.killa.startswith("/"):
            raise ValueError(
                "Killa number cannot start with '/'."
            )

        if self.killa.endswith("/"):
            raise ValueError(
                "Killa number cannot end with '/'."
            )

        if "//" in self.killa:
            raise ValueError(
                "Killa number cannot contain '//'."
            )

    # ---------------------------------------------------------
    # Formatting
    # ---------------------------------------------------------

    def display(
        self,
    ) -> str:
        """
        Return long display format.
        """

        return (
            f"Rectangle {self.rectangle} "
            f"Killa {self.killa}"
        )

    def __str__(
        self,
    ) -> str:
        """
        Return compact format.
        """

        return (
            f"{self.rectangle}//{self.killa}"
        )

    def __repr__(
        self,
    ) -> str:
        """
        Developer representation.
        """

        return (
            "ParcelNumber("
            f"{self.rectangle}//{self.killa}"
            ")"
        )