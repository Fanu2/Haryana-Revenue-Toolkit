"""
Unit tests for BaseEntity.
"""

from __future__ import annotations

from datetime import UTC
from time import sleep
from uuid import UUID

from hrtk.domain.base_entity import BaseEntity


def test_id_is_uuid() -> None:
    """Entity should have a UUID."""
    entity = BaseEntity()

    assert isinstance(entity.id, UUID)


def test_created_at_exists() -> None:
    """created_at should exist."""
    entity = BaseEntity()

    assert entity.created_at.tzinfo == UTC


def test_updated_at_exists() -> None:
    """updated_at should exist."""
    entity = BaseEntity()

    assert entity.updated_at.tzinfo == UTC


def test_touch_updates_timestamp() -> None:
    """touch() should update updated_at."""
    entity = BaseEntity()

    previous = entity.updated_at

    sleep(0.001)

    entity.touch()

    assert entity.updated_at > previous


def test_identity_property() -> None:
    """identity should return id."""
    entity = BaseEntity()

    assert entity.identity == entity.id


def test_repr_contains_class_name() -> None:
    """repr() should identify the class."""
    entity = BaseEntity()

    assert "BaseEntity" in repr(entity)