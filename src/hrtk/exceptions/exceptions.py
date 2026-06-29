"""
HRTK custom exceptions.
"""


class HRTKError(Exception):
    """
    Base exception for HRTK.
    """


class DomainValidationError(HRTKError):
    """
    Raised when domain validation fails.
    """


class RepositoryError(HRTKError):
    """
    Repository operation failed.
    """


class ServiceError(HRTKError):
    """
    Service operation failed.
    """