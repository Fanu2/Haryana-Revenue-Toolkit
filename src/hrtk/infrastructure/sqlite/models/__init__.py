"""
SQLite model registrations.

Importing this package registers all SQLAlchemy models.
"""

from hrtk.infrastructure.sqlite.models.village_model import VillageModel
from hrtk.infrastructure.sqlite.models.owner_model import OwnerModel
from hrtk.infrastructure.sqlite.models.khewat_model import KhewatModel
from hrtk.infrastructure.sqlite.models.parcel_model import ParcelModel
from hrtk.infrastructure.sqlite.models.ownership_model import OwnershipModel
from hrtk.infrastructure.sqlite.models.khewat_parcel_model import (
    KhewatParcelModel,
)
from hrtk.infrastructure.sqlite.models.jamabandi_model import JamabandiModel
from hrtk.infrastructure.sqlite.models.partition_case_model import (
    PartitionCaseModel,
)
from hrtk.infrastructure.sqlite.models.partition_allocation_model import (
    PartitionAllocationModel,
)

__all__ = [
    "VillageModel",
    "OwnerModel",
    "KhewatModel",
    "ParcelModel",
    "OwnershipModel",
    "KhewatParcelModel",
    "JamabandiModel",
    "PartitionCaseModel",
    "PartitionAllocationModel",
]
