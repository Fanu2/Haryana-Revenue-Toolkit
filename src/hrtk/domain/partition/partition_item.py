from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(slots=True)
class PartitionItem:
    """
    Represents one parcel allocation within a partition.
    """

    id: UUID = field(default_factory=uuid4)

    partition_id: UUID | None = None

    parcel_id: UUID | None = None
    owner_id: UUID | None = None

    old_share: float = 0.0
    new_share: float = 0.0

    area_before: float = 0.0
    area_after: float = 0.0

    mutation_required: bool = False

    remarks: str = ""