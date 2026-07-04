"""
Haryana Revenue Toolkit (HRTK)

Base Seeder.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from time import perf_counter
from typing import Any


class BaseSeeder(ABC):
    """
    Base class for every HRTK demo data seeder.
    """

    def __init__(
        self,
        context: Any,
    ) -> None:

        self._context = context

        self._created = 0
        self._skipped = 0
        self._errors = 0

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def context(
        self,
    ) -> Any:
        return self._context

    @property
    def created(
        self,
    ) -> int:
        return self._created

    @property
    def skipped(
        self,
    ) -> int:
        return self._skipped

    @property
    def errors(
        self,
    ) -> int:
        return self._errors

    @property
    def name(
        self,
    ) -> str:
        return self.__class__.__name__

    # ---------------------------------------------------------
    # Counters
    # ---------------------------------------------------------

    def created_one(
        self,
    ) -> None:

        self._created += 1

    def skipped_one(
        self,
    ) -> None:

        self._skipped += 1

    def error_one(
        self,
    ) -> None:

        self._errors += 1

    # ---------------------------------------------------------
    # Runner
    # ---------------------------------------------------------

    def run(
        self,
    ) -> None:

        start = perf_counter()

        print()

        print("=" * 60)

        print(self.name)

        print("=" * 60)

        self.seed()

        elapsed = perf_counter() - start

        print()

        print(f"Created : {self.created}")
        print(f"Skipped : {self.skipped}")
        print(f"Errors  : {self.errors}")
        print(f"Elapsed : {elapsed:.3f} sec")

    # ---------------------------------------------------------
    # Abstract
    # ---------------------------------------------------------

    @abstractmethod
    def seed(
        self,
    ) -> None:
        """
        Execute the seeding process.
        """
        raise NotImplementedError