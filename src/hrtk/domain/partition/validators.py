from uuid import UUID

from .exceptions import InvalidPartitionError
from .partition import Partition
from .partition_item import PartitionItem


def validate_uuid(value: UUID | None, field_name: str) -> None:
    """Validate that a value is either None or a UUID."""
    if value is None:
        return

    if not isinstance(value, UUID):
        raise InvalidPartitionError(f"{field_name} must be a UUID.")


def validate_partition(partition: Partition) -> None:
    """Basic structural validation for a Partition."""

    validate_uuid(partition.id, "id")
    validate_uuid(partition.village_id, "village_id")
    validate_uuid(partition.jamabandi_id, "jamabandi_id")

    if not partition.partition_number.strip():
        raise InvalidPartitionError("Partition number is required.")


def validate_partition_item(item: PartitionItem) -> None:
    """Basic structural validation for a PartitionItem."""

    validate_uuid(item.id, "id")
    validate_uuid(item.partition_id, "partition_id")
    validate_uuid(item.parcel_id, "parcel_id")
    validate_uuid(item.owner_id, "owner_id")

    if item.area_before < 0:
        raise InvalidPartitionError("Area before cannot be negative.")

    if item.area_after < 0:
        raise InvalidPartitionError("Area after cannot be negative.")