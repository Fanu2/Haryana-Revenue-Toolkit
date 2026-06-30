"""
Haryana Revenue Toolkit (HRTK)

Integration tests for SQLiteOwnerRepository.
"""

from __future__ import annotations

from uuid import uuid4

from hrtk.domain.owner import Owner
from hrtk.infrastructure.sqlite.database import (
    reset_database,
)
from hrtk.infrastructure.sqlite.sqlite_owner_repository import (
    SQLiteOwnerRepository,
)


def test_add_and_get_owner() -> None:
    """
    Save and reload an owner.
    """

    reset_database()

    repository = SQLiteOwnerRepository()

    village_id = uuid4()

    owner = Owner(
        village_id=village_id,
        owner_code="OWN001",
        owner_name="Jasvir Singh",
        father_name="Gurdev Singh",
        address="Taruana",
        mobile="9876543210",
        remarks="Integration Test",
    )

    repository.add(owner)

    loaded = repository.get("OWN001")

    assert loaded is not None
    assert loaded.owner_code == "OWN001"
    assert loaded.owner_name == "Jasvir Singh"
    assert loaded.father_name == "Gurdev Singh"
    assert loaded.address == "Taruana"
    assert loaded.mobile == "9876543210"
    assert loaded.remarks == "Integration Test"
    assert loaded.village_id == village_id
    assert loaded.active is True


def test_find_by_village() -> None:
    """
    Find owners belonging to a village.
    """

    reset_database()

    repository = SQLiteOwnerRepository()

    village_id = uuid4()

    owner1 = Owner(
        village_id=village_id,
        owner_code="OWN101",
        owner_name="Owner One",
    )

    owner2 = Owner(
        village_id=village_id,
        owner_code="OWN102",
        owner_name="Owner Two",
    )

    repository.add(owner1)
    repository.add(owner2)

    owners = repository.find_by_village(village_id)

    assert len(owners) == 2

    codes = {owner.owner_code for owner in owners}

    assert "OWN101" in codes
    assert "OWN102" in codes