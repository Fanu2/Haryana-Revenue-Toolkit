"""
Haryana Revenue Toolkit (HRTK)

Partition Status.
"""

from __future__ import annotations

from enum import Enum


class PartitionStatus(
    Enum,
):
    """
    Status of a partition case.
    """

    DRAFT = "Draft"

    VALIDATED = "Validated"

    COMPLETED = "Completed"

    CANCELLED = "Cancelled"

    @property
    def display_name(
        self,
    ) -> str:
        """
        Return display name.
        """

        return self.value

    def __str__(
        self,
    ) -> str:

        return self.value