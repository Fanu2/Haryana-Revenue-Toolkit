"""
Haryana Revenue Toolkit (HRTK)

Allocation Controller.
"""

from __future__ import annotations

from hrtk.application.application_context import (
    ApplicationContext,
)

from hrtk.presentation.partition.partition_widget import (
    PartitionWidget,
)


class AllocationController:
    """
    Coordinates Allocation workflow between
    the Partition Workbench and the
    Allocation Service.
    """

    def __init__(
        self,
        context: ApplicationContext,
        widget: PartitionWidget,
    ) -> None:

        self._context = context

        self._widget = widget

    # ---------------------------------------------------------
    # Commands
    # ---------------------------------------------------------

    def allocate(
        self,
    ) -> None:
        """
        Allocate land to the selected owner.

        Implementation added in A4.2.
        """

        pass

    def undo(
        self,
    ) -> None:
        """
        Undo last allocation.

        Implementation added in A4.3.
        """

        pass

    def clear(
        self,
    ) -> None:
        """
        Clear current allocations.

        Implementation added in A4.3.
        """

        pass