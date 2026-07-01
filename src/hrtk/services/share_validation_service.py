"""
Haryana Revenue Toolkit (HRTK)

Share Validation Service.
"""

from __future__ import annotations

from hrtk.domain.ownership import Ownership
from hrtk.domain.value_objects.fraction import Fraction


class ShareValidationService:
    """
    Business rules for validating ownership shares.
    """

    @staticmethod
    def total_share(
        ownerships: list[Ownership],
    ) -> Fraction:
        """
        Return the total ownership share.
        """

        total = Fraction(0, 1)

        for ownership in ownerships:
            total += ownership.share

        return total

    @staticmethod
    def is_complete(
        ownerships: list[Ownership],
    ) -> bool:
        """
        True if ownership totals exactly 100%.
        """

        return (
            ShareValidationService.total_share(
                ownerships,
            )
            == Fraction(1, 1)
        )

    @staticmethod
    def exceeds_limit(
        ownerships: list[Ownership],
    ) -> bool:
        """
        True if ownership exceeds 100%.
        """

        return (
            ShareValidationService.total_share(
                ownerships,
            )
            > Fraction(1, 1)
        )

    @staticmethod
    def remaining_share(
        ownerships: list[Ownership],
    ) -> Fraction:
        """
        Return the remaining ownership available.
        """

        return (
            Fraction(1, 1)
            - ShareValidationService.total_share(
                ownerships,
            )
        )