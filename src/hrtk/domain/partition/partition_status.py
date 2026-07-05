from enum import Enum


class PartitionStatus(str, Enum):
    """
    Lifecycle status of a partition proceeding.
    """

    DRAFT = "Draft"
    UNDER_VERIFICATION = "UnderVerification"
    APPROVED = "Approved"
    IMPLEMENTED = "Implemented"
    CANCELLED = "Cancelled"