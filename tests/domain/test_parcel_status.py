"""
Haryana Revenue Toolkit (HRTK)

Unit tests for ParcelStatus.
"""

from __future__ import annotations

from hrtk.domain.parcel_status import ParcelStatus


def test_active() -> None:
    assert str(ParcelStatus.ACTIVE) == "Active"


def test_historical() -> None:
    assert str(ParcelStatus.HISTORICAL) == "Historical"


def test_merged() -> None:
    assert str(ParcelStatus.MERGED) == "Merged"


def test_cancelled() -> None:
    assert str(ParcelStatus.CANCELLED) == "Cancelled"


def test_corrected() -> None:
    assert str(ParcelStatus.CORRECTED) == "Corrected"


def test_unknown() -> None:
    assert str(ParcelStatus.UNKNOWN) == "Unknown"