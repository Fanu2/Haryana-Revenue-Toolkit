"""
Haryana Revenue Toolkit (HRTK)

Share Value Object.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(
    frozen=True,
    slots=True,
)
class Share:
    """
    Immutable ownership share.

    Internally backed by Python's
    Fraction class.
    """

    numerator: int

    denominator: int

    def __post_init__(self) -> None:
        """
        Validate share.
        """

        if self.numerator < 0:
            raise ValueError(
                "Numerator cannot be negative."
            )

        if self.denominator <= 0:
            raise ValueError(
                "Denominator must be greater than zero."
            )

        fraction = Fraction(
            self.numerator,
            self.denominator,
        )

        object.__setattr__(
            self,
            "numerator",
            fraction.numerator,
        )

        object.__setattr__(
            self,
            "denominator",
            fraction.denominator,
        )

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def fraction(
        self,
    ) -> Fraction:
        """
        Return Fraction object.
        """

        return Fraction(
            self.numerator,
            self.denominator,
        )

    @property
    def percentage(
        self,
    ) -> float:
        """
        Return ownership percentage.
        """

        return float(self.fraction * 100)

    # ---------------------------------------------------------
    # Formatting
    # ---------------------------------------------------------

    def display(
        self,
    ) -> str:
        """
        Long display.
        """

        return (
            f"{self.numerator} Share "
            f"out of {self.denominator}"
        )

    def __str__(
        self,
    ) -> str:

        return (
            f"{self.numerator}/"
            f"{self.denominator}"
        )

    def __repr__(
        self,
    ) -> str:

        return (
            f"Share("
            f"{self.numerator}/"
            f"{self.denominator})"
        )

    # ---------------------------------------------------------
    # Arithmetic
    # ---------------------------------------------------------

    def __add__(
        self,
        other: object,
    ) -> "Share":

        if not isinstance(
            other,
            Share,
        ):
            return NotImplemented

        value = (
            self.fraction
            + other.fraction
        )

        return Share(
            value.numerator,
            value.denominator,
        )

    def __sub__(
        self,
        other: object,
    ) -> "Share":

        if not isinstance(
            other,
            Share,
        ):
            return NotImplemented

        value = (
            self.fraction
            - other.fraction
        )

        if value < 0:
            raise ValueError(
                "Share cannot become negative."
            )

        return Share(
            value.numerator,
            value.denominator,
        )