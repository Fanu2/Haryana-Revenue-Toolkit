"""
Haryana Revenue Toolkit (HRTK)

Parcel Mapper.
"""

from __future__ import annotations

from hrtk.domain.parcel import Parcel


class ParcelMapper:
    """
    Converts between persistence models
    and Parcel domain objects.

    SQLite implementation will be added
    in the next sprint.
    """

    @staticmethod
    def to_domain(model) -> Parcel:
        """
        Convert a persistence model to a
        Parcel domain object.
        """
        raise NotImplementedError

    @staticmethod
    def to_model(parcel: Parcel):
        """
        Convert a Parcel domain object to
        a persistence model.
        """
        raise NotImplementedError