"""
Haryana Revenue Toolkit (HRTK)

Generic repository.
"""

from __future__ import annotations

from typing import Generic, Iterator, TypeVar
from uuid import UUID

from hrtk.domain.base_entity import BaseEntity
from hrtk.exceptions.exceptions import (
    DuplicateEntityError,
    EntityNotFoundError,
)

T = TypeVar("T", bound=BaseEntity)


class BaseRepository(Generic[T]):
    """
    Generic in-memory repository for domain entities.
    """

    def __init__(self) -> None:
        self._items: dict[UUID, T] = {}

    def add(self, entity: T) -> None:
        """
        Add an entity.

        Raises
        ------
        DuplicateEntityError
            If the entity already exists.
        """
        if entity.id in self._items:
            raise DuplicateEntityError(
                f"Entity with id {entity.id} already exists."
            )

        self._items[entity.id] = entity

    def update(self, entity: T) -> None:
        """
        Update an existing entity.

        Raises
        ------
        EntityNotFoundError
            If the entity does not exist.
        """
        if entity.id not in self._items:
            raise EntityNotFoundError(
                f"Entity with id {entity.id} was not found."
            )

        self._items[entity.id] = entity

    def remove(self, entity: T) -> None:
        """
        Remove an entity.

        Raises
        ------
        EntityNotFoundError
            If the entity does not exist.
        """
        if entity.id not in self._items:
            raise EntityNotFoundError(
                f"Entity with id {entity.id} was not found."
            )

        del self._items[entity.id]

    def get(self, entity_id: UUID) -> T | None:
        """
        Return an entity by its identifier.
        """
        return self._items.get(entity_id)

    def exists(self, entity_id: UUID) -> bool:
        """
        Return True if an entity exists.
        """
        return entity_id in self._items

    def all(self) -> list[T]:
        """
        Return all entities.
        """
        return list(self._items.values())

    def count(self) -> int:
        """
        Return the number of entities.
        """
        return len(self._items)

    def clear(self) -> None:
        """
        Remove all entities.
        """
        self._items.clear()

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items.values())

    def __contains__(self, entity: object) -> bool:
        if not isinstance(entity, BaseEntity):
            return False

        return entity.id in self._items

    def __bool__(self) -> bool:
        return bool(self._items)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(count={len(self)})"
        )