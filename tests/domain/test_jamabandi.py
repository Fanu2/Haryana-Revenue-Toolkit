"""
Haryana Revenue Toolkit (HRTK)

Tests for Jamabandi.
"""

from uuid import uuid4

from hrtk.domain.jamabandi import (
    Jamabandi,
)


def test_create_jamabandi():

    village_id = uuid4()

    jamabandi = Jamabandi(
        id=uuid4(),
        village_id=village_id,
        year="2025-26",
    )

    assert jamabandi.village_id == village_id

    assert jamabandi.year == "2025-26"

    assert jamabandi.active

    assert not jamabandi.finalized


def test_finalize():

    jamabandi = Jamabandi(
        id=uuid4(),
        village_id=uuid4(),
        year="2025-26",
    )

    jamabandi.finalize()

    assert jamabandi.finalized


def test_reopen():

    jamabandi = Jamabandi(
        id=uuid4(),
        village_id=uuid4(),
        year="2025-26",
    )

    jamabandi.finalize()

    jamabandi.reopen()

    assert not jamabandi.finalized