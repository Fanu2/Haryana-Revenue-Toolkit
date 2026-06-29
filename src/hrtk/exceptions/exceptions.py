"""
Haryana Revenue Toolkit (HRTK)

Custom exceptions.
"""

from __future__ import annotations


class HRTKError(Exception):
    """
    Base exception for HRTK.
    """

    pass


# ---------------------------------------------------------------------
# Domain
# ---------------------------------------------------------------------


class DomainValidationError(HRTKError):
    """
    Raised when domain validation fails.
    """

    pass


# ---------------------------------------------------------------------
# Repository
# ---------------------------------------------------------------------


class RepositoryError(HRTKError):
    """
    Base class for repository exceptions.
    """

    pass


class EntityNotFoundError(RepositoryError):
    """
    Raised when an entity cannot be found.
    """

    pass


class DuplicateEntityError(RepositoryError):
    """
    Raised when an entity already exists.
    """

    pass


# ---------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------


class ServiceError(HRTKError):
    """
    Base class for service exceptions.
    """

    pass