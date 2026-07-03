"""
Haryana Revenue Toolkit (HRTK)

Validation Service.
"""

from __future__ import annotations

from hrtk.domain.partition_case import (
    PartitionCase,
)

from hrtk.domain.partition_allocation import (
    PartitionAllocation,
)


class ValidationService:
    """
    Performs business validation for
    Partition Cases.
    """

    def __init__(
        self,
    ) -> None:
        pass

    # ---------------------------------------------------------
    # Basic Validation
    # ---------------------------------------------------------

    def validate_case(
        self,
        case: PartitionCase,
    ) -> list[str]:
        """
        Validate a partition case.

        Returns a list of validation errors.
        """

        errors: list[str] = []

        if not case.has_allocations:

            errors.append(
                "No allocations exist."
            )

        return errors

    def is_valid(
        self,
        case: PartitionCase,
    ) -> bool:
        """
        Return True if the case
        contains no validation errors.
        """

        return (
            len(
                self.validate_case(
                    case,
                )
            )
            == 0
        )
    
    # ---------------------------------------------------------
    # Allocation Validation
    # ---------------------------------------------------------

    def validate_allocation(
        self,
        case: PartitionCase,
        allocation: PartitionAllocation,
    ) -> list[str]:
        """
        Validate one allocation.
        """

        errors: list[str] = []

        if allocation.is_empty:

            errors.append(
                "Allocated area is zero."
            )

        return errors
    
    # ---------------------------------------------------------
    # Convenience
    # ---------------------------------------------------------

    def can_allocate(
        self,
        case: PartitionCase,
        allocation: PartitionAllocation,
    ) -> bool:
        """
        Return True if allocation
        passes validation.
        """

        return (
            len(
                self.validate_allocation(
                    case,
                    allocation,
                )
            )
            == 0
        )
    
