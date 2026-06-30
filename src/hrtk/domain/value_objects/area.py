"""
Haryana Revenue Toolkit (HRTK)

Area Value Object.
"""

from __future__ import annotations

from dataclasses import dataclass

from hrtk.constants.area import (
    MARLA_PER_KANAL,
    SARSAI_PER_KANAL,
    SARSAI_PER_MARLA,
)


@dataclass(
    frozen=True,
    slots=True,
)
class Area:
    """
    Immutable land area.

    Internally stored as total Sarsai.
    """

    total_sarsai: int

    def __post_init__(self) -> None:
        """
        Validate the area.
        """

        if self.total_sarsai < 0:
            raise ValueError(
                "Area cannot be negative."
            )

    # ---------------------------------------------------------
    # Factory Methods
    # ---------------------------------------------------------

    @classmethod
    def zero(
        cls,
    ) -> "Area":
        """
        Return zero area.
        """

        return cls(0)

    @classmethod
    def from_total_sarsai(
        cls,
        total_sarsai: int,
    ) -> "Area":
        """
        Construct an Area from total Sarsai.
        """

        return cls(total_sarsai)

    @classmethod
    def from_kms(
        cls,
        kanal: int = 0,
        marla: int = 0,
        sarsai: int = 0,
    ) -> "Area":
        """
        Construct an Area from
        Kanal-Marla-Sarsai.
        """

        if kanal < 0:
            raise ValueError(
                "Kanal cannot be negative."
            )

        if marla < 0:
            raise ValueError(
                "Marla cannot be negative."
            )

        if sarsai < 0:
            raise ValueError(
                "Sarsai cannot be negative."
            )

        total = (
            kanal * SARSAI_PER_KANAL
            + marla * SARSAI_PER_MARLA
            + sarsai
        )

        return cls(total)

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def kanal(
        self,
    ) -> int:
        """
        Return Kanal.
        """

        return (
            self.total_sarsai //
            SARSAI_PER_KANAL
        )

    @property
    def marla(
        self,
    ) -> int:
        """
        Return Marla.
        """

        remaining = (
            self.total_sarsai %
            SARSAI_PER_KANAL
        )

        return (
            remaining //
            SARSAI_PER_MARLA
        )

    @property
    def sarsai(
        self,
    ) -> int:
        """
        Return Sarsai.
        """

        return (
            self.total_sarsai %
            SARSAI_PER_MARLA
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
            f"{self.kanal} Kanal "
            f"{self.marla} Marla "
            f"{self.sarsai} Sarsai"
        )

    def __str__(
        self,
    ) -> str:
        """
        Return compact display.
        """

        return (
            f"{self.kanal}K-"
            f"{self.marla}M-"
            f"{self.sarsai}S"
        )

    def __repr__(
        self,
    ) -> str:
        """
        Return developer representation.
        """

        return (
            f"Area("
            f"{self.kanal}K "
            f"{self.marla}M "
            f"{self.sarsai}S)"
        )

    # ---------------------------------------------------------
    # Arithmetic
    # ---------------------------------------------------------

    def __add__(
        self,
        other: object,
    ) -> "Area":

        if not isinstance(
            other,
            Area,
        ):
            return NotImplemented

        return Area.from_total_sarsai(
            self.total_sarsai
            + other.total_sarsai
        )

    def __sub__(
        self,
        other: object,
    ) -> "Area":

        if not isinstance(
            other,
            Area,
        ):
            return NotImplemented

        total = (
            self.total_sarsai
            - other.total_sarsai
        )

        if total < 0:
            raise ValueError(
                "Area cannot become negative."
            )

        return Area.from_total_sarsai(
            total,
        )