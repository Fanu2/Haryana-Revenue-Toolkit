"""
Haryana Revenue Toolkit (HRTK)

Allocation Validator.
"""

from __future__ import annotations

from hrtk.domain.ownership import Ownership
from hrtk.domain.parcel import Parcel


class AllocationValidator:
    """
    Performs presentation-layer validation
    before invoking AllocationService.
    """

    def validate(
        self,
        ownership: Ownership | None,
        parcel: Parcel | None,
    ) -> tuple[
        bool,
        str,
    ]:
        """
        Validate user selections.
        """

        if ownership is None:

            return (
                False,
                "Select an owner.",
            )

        if parcel is None:

            return (
                False,
                "Select a Khasra.",
            )

        return (
            True,
            "",
        )