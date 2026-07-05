class PartitionError(Exception):
    """Base exception for all partition-related errors."""


class DuplicatePartitionError(PartitionError):
    """Raised when a duplicate partition is detected."""


class InvalidPartitionError(PartitionError):
    """Raised when partition data is invalid."""


class AreaMismatchError(PartitionError):
    """Raised when partition areas do not balance."""


class OwnerShareMismatchError(PartitionError):
    """Raised when owner shares are inconsistent."""


class ParcelAlreadyAllocatedError(PartitionError):
    """Raised when a parcel is already allocated."""