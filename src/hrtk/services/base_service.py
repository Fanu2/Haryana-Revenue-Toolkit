"""
Haryana Revenue Toolkit (HRTK)

Generic application service.
"""

from __future__ import annotations

from typing import Generic, TypeVar
from uuid import UUID

from hrtk.domain.base_entity import BaseEntity
from hrtk.repositories.base_repository import BaseRepository


T = TypeVar("T", bound=BaseEntity)


class BaseService(Generic[T]):
    """
    Base class for application services.

    Coordinates access to repositories while allowing
    derived services to implement business operations.
    """

    def __init__(
        self,
        repository: BaseRepository[T],
    ) -> None:
        self._repository = repository

    @property
    def repository(self) -> BaseRepository[T]:
        """
        Return the underlying repository.
        """
        return self._repository

    def get(
        self,
        entity_id: UUID,
    ) -> T | None:
        """
        Return an entity by its identifier.
        """
        return self.repository.get(entity_id)

    def all(self) -> list[T]:
        """
        Return all entities.
        """
        return self.repository.all()

    def exists(
        self,
        entity_id: UUID,
    ) -> bool:
        """
        Return True if an entity exists.
        """
        return self.repository.exists(entity_id)

    def count(self) -> int:
        """
        Return the number of entities.
        """
        return self.repository.count()

    def __len__(self) -> int:
        return self.count()

    def __bool__(self) -> bool:
        return self.count() > 0

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(count={self.count()})"
        )