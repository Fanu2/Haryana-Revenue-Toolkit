"""
Haryana Revenue Toolkit (HRTK)

Fraction Value Object.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True, slots=True)
class Fraction:
    """
    Exact mathematical fraction.

    Examples

        1/2
        5/16
        17/144
    """

    numerator: int
    denominator: int

    def __post_init__(self) -> None:

        if self.denominator == 0:
            raise ValueError(
                "Denominator cannot be zero."
            )

        if self.numerator < 0:
            raise ValueError(
                "Numerator cannot be negative."
            )

        if self.denominator < 0:
            raise ValueError(
                "Denominator cannot be negative."
            )

        d = gcd(
            self.numerator,
            self.denominator,
        )

        object.__setattr__(
            self,
            "numerator",
            self.numerator // d,
        )

        object.__setattr__(
            self,
            "denominator",
            self.denominator // d,
        )

    @property
    def percentage(
        self,
    ) -> float:

        return (
            self.numerator
            / self.denominator
            * 100
        )

    def __str__(
        self,
    ) -> str:

        return (
            f"{self.numerator}/"
            f"{self.denominator}"
        )
    

        # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def is_zero(
        self,
    ) -> bool:

        return self.numerator == 0

    def is_whole(
        self,
    ) -> bool:

        return (
            self.numerator
            == self.denominator
        )

    @classmethod
    def from_string(
        cls,
        value: str,
    ) -> "Fraction":

        value = value.strip()

        numerator, denominator = value.split("/")

        return cls(
            int(numerator),
            int(denominator),
        )

    def __float__(
        self,
    ) -> float:
        """
        Return decimal representation.
        """

        return (
            self.numerator
            / self.denominator
        )

    # ---------------------------------------------------------
    # Arithmetic
    # ---------------------------------------------------------

    def __add__(
        self,
        other: "Fraction",
    ) -> "Fraction":

        return Fraction(
            self.numerator * other.denominator
            + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __sub__(
        self,
        other: "Fraction",
    ) -> "Fraction":

        return Fraction(
            self.numerator * other.denominator
            - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __mul__(
        self,
        other: "Fraction",
    ) -> "Fraction":

        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )

    def __truediv__(
        self,
        other: "Fraction",
    ) -> "Fraction":

        if other.numerator == 0:
            raise ZeroDivisionError(
                "Cannot divide by zero fraction."
            )

        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator,
        )

    # ---------------------------------------------------------
    # Comparisons
    # ---------------------------------------------------------

    def __lt__(
        self,
        other: "Fraction",
    ) -> bool:

        return (
            self.numerator * other.denominator
            <
            other.numerator * self.denominator
        )

    def __le__(
        self,
        other: "Fraction",
    ) -> bool:

        return (
            self.numerator * other.denominator
            <=
            other.numerator * self.denominator
        )

    def __gt__(
        self,
        other: "Fraction",
    ) -> bool:

        return (
            self.numerator * other.denominator
            >
            other.numerator * self.denominator
        )

    def __ge__(
        self,
        other: "Fraction",
    ) -> bool:

        return (
            self.numerator * other.denominator
            >=
            other.numerator * self.denominator
        )