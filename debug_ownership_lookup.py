"""
Debug Ownership Lookup

Checks whether Ownership.owner_id values
match Owner.id values.
"""

from hrtk.application.application_context import (
    ApplicationContext,
)

ctx = ApplicationContext()

print("=" * 70)
print("OWNERS")
print("=" * 70)

owners = ctx.owner_service.all()

owner_lookup = {}

for owner in owners:
    owner_lookup[str(owner.id)] = owner.display_name
    print(
        owner.id,
        "->",
        owner.display_name,
    )

print()

print("=" * 70)
print("OWNERSHIPS")
print("=" * 70)

ownerships = ctx.ownership_service.all()

for ownership in ownerships:

    owner_uuid = str(ownership.owner_id)

    print("Ownership ID :", ownership.id)
    print("Owner UUID   :", owner_uuid)

    if owner_uuid in owner_lookup:

        print(
            "MATCH       :",
            owner_lookup[owner_uuid],
        )

    else:

        print("MATCH       : UNKNOWN")

    print("-" * 70)