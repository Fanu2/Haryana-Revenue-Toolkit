"""
Haryana Revenue Toolkit (HRTK)

Validation Service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.domain.owner import Owner

from hrtk.domain.parcel import Parcel

from hrtk.services.calculation_service import (
    CalculationService,
)


class ValidationService:
    """
    Performs business validation
    for Partition proceedings.

    No persistence.

    No UI.

    No calculations.
    """

    def __init__(
        self,
        calculation_service: CalculationService,
    ) -> None:

        self._calculation_service = (
            calculation_service
        )

    # ---------------------------------------------------------
    # Owner Validation
    # ---------------------------------------------------------

    def owner_has_allocation(
        self,
        case_id: UUID,
        owner: Owner,
    ) -> bool:
        """
        Return True if the owner
        has allocations.
        """

        return (
            self._calculation_service.owner_has_allocation(
                case_id,
                owner,
            )
        )

    def owner_is_valid(
        self,
        case_id: UUID,
        owner: Owner,
    ) -> bool:
        """
        Validate owner allocation.
        """

        return (
            self.owner_has_allocation(
                case_id,
                owner,
            )
        )
    
    # ---------------------------------------------------------
    # Parcel Validation
    # ---------------------------------------------------------

    def parcel_is_complete(
        self,
        case_id: UUID,
        parcel: Parcel,
    ) -> bool:
        """
        Return True if parcel
        allocation is complete.
        """

        return (
            self._calculation_service.parcel_is_complete(
                case_id,
                parcel,
            )
        )

    def parcel_is_valid(
        self,
        case_id: UUID,
        parcel: Parcel,
    ) -> bool:
        """
        Validate parcel.
        """

        return (
            self.parcel_is_complete(
                case_id,
                parcel,
            )
        )
    
    # ---------------------------------------------------------
    # Case Validation
    # ---------------------------------------------------------

    def has_allocations(
        self,
        case_id: UUID,
    ) -> bool:
        """
        Return True if allocations exist.
        """

        return (
            self._calculation_service.has_allocations(
                case_id,
            )
        )

    def case_is_valid(
        self,
        case_id: UUID,
    ) -> bool:
        """
        Validate the partition case.
        """

        return (
            self.has_allocations(
                case_id,
            )
        )
    
    # ---------------------------------------------------------
    # Overall Validation
    # ---------------------------------------------------------

    def overall_status(
        self,
        case_id: UUID,
    ) -> bool:
        """
        Return overall validation status.
        """

        return (
            self.case_is_valid(
                case_id,
            )
        )
    
