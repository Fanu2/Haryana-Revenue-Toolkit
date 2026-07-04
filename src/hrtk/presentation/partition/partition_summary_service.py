"""
Haryana Revenue Toolkit (HRTK)

Partition Summary Service.
"""

from __future__ import annotations

from uuid import UUID

from hrtk.services.calculation_service import (
    CalculationService,
)

from hrtk.services.validation_service import (
    ValidationService,
)


class PartitionSummaryService:
    """
    Provides formatted summary data
    for the Partition Workbench.

    This service contains no UI code.
    """

    def __init__(
        self,
        calculation_service: CalculationService,
        validation_service: ValidationService,
    ) -> None:

        self._calculation_service = (
            calculation_service
        )

        self._validation_service = (
            validation_service
        )

