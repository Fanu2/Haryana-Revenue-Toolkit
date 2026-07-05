from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import UUID, uuid4

from .partition_status import PartitionStatus


@dataclass(slots=True)
class Partition:
    """
    Represents one partition proceeding.
    """

    id: UUID = field(default_factory=uuid4)

    village_id: UUID | None = None
    jamabandi_id: UUID | None = None

    partition_number: str = ""
    application_number: str = ""

    application_date: date | None = None
    effective_date: date | None = None

    status: PartitionStatus = PartitionStatus.DRAFT

    remarks: str = ""

    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)