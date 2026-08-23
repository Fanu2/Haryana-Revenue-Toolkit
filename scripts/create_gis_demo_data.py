import sqlite3
import uuid
from pathlib import Path


DB = Path(
    "demo/database/hrtk_demo.db"
)


def uid():
    return str(uuid.uuid4())


conn = sqlite3.connect(DB)

cur = conn.cursor()


# =================================================
# Village
# =================================================

cur.execute(
    """
    SELECT id
    FROM villages
    WHERE code=?
    """,
    ("HRK001",)
)

row = cur.fetchone()


if row:

    village_id = row[0]

else:

    village_id = uid()

    cur.execute(
        """
        INSERT INTO villages
        (
            id,
            code,
            name,
            tehsil,
            district,
            state,
            active
        )
        VALUES (?,?,?,?,?,?,?)
        """,
        (
            village_id,
            "HRK001",
            "Chautala",
            "Dabwali",
            "Sirsa",
            "Haryana",
            1
        )
    )



# =================================================
# Owners
# =================================================

owners = {}


owner_data = [

    (
        "OWN001",
        "Jasvir Singh",
        "Gurcharan Singh"
    ),

    (
        "OWN002",
        "Baldev Singh",
        "Kartar Singh"
    ),

]


for code, name, father in owner_data:


    cur.execute(
        """
        SELECT id
        FROM owners
        WHERE owner_code=?
        """,
        (code,)
    )


    row = cur.fetchone()


    if row:

        owner_id = row[0]


    else:

        cur.execute(
            """
            INSERT INTO owners
            (
                village_id,
                owner_code,
                owner_name,
                father_name,
                address,
                mobile,
                remarks,
                active
            )
            VALUES (?,?,?,?,?,?,?,?)
            """,
            (
                village_id,
                code,
                name,
                father,
                "Chautala, Sirsa",
                "",
                "Demo owner",
                1
            )
        )


        owner_id = cur.lastrowid


    owners[code] = owner_id



# =================================================
# Khewat
# =================================================

cur.execute(
    """
    SELECT id
    FROM khewats
    WHERE village_id=? AND khewat_no=?
    """,
    (
        village_id,
        "42"
    )
)


row = cur.fetchone()


if row:

    khewat_id = row[0]


else:

    khewat_id = uid()


    cur.execute(
        """
        INSERT INTO khewats
        (
            id,
            village_id,
            khewat_no,
            old_khewat_no,
            jamabandi_year,
            remarks,
            active
        )
        VALUES (?,?,?,?,?,?,?)
        """,
        (
            khewat_id,
            village_id,
            "42",
            "18",
            "2025-26",
            "Demo Khewat",
            1
        )
    )



# =================================================
# Parcels
# =================================================

parcels = [

    (
        15,
        "7",
        5,
        10
    ),

    (
        15,
        "8",
        4,
        0
    ),

]


for rectangle, killa, kanal, marla in parcels:


    cur.execute(
        """
        SELECT id
        FROM parcels
        WHERE rectangle=? AND killa=?
        """,
        (
            rectangle,
            killa
        )
    )


    row = cur.fetchone()


    if not row:

        cur.execute(
            """
            INSERT INTO parcels
            (
                rectangle,
                killa,
                kanal,
                marla,
                sarsai,
                remarks,
                status,
                active
            )
            VALUES (?,?,?,?,?,?,?,?)
            """,
            (
                rectangle,
                killa,
                kanal,
                marla,
                0,
                "Demo agricultural land",
                "active",
                1
            )
        )



# =================================================
# Ownership
# =================================================

ownership_data = [

    (
        owners["OWN001"],
        1,
        2
    ),

    (
        owners["OWN002"],
        1,
        2
    )

]


for owner_id, numerator, denominator in ownership_data:


    cur.execute(
        """
        SELECT id
        FROM ownerships
        WHERE owner_id=? AND khewat_id=?
        """,
        (
            owner_id,
            khewat_id
        )
    )


    row = cur.fetchone()


    if not row:

        cur.execute(
            """
            INSERT INTO ownerships
            (
                id,
                owner_id,
                khewat_id,
                numerator,
                denominator,
                remarks,
                active
            )
            VALUES (?,?,?,?,?,?,?)
            """,
            (
                uid(),
                owner_id,
                khewat_id,
                numerator,
                denominator,
                "Equal share",
                1
            )
        )



conn.commit()


conn.close()


print(
    "HRTK GIS demo data created successfully"
)