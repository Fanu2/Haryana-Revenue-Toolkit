"""
Haryana Revenue Toolkit (HRTK)

Development Sample Data.
"""

from __future__ import annotations

# ==========================================================
# Geography
# ==========================================================

STATE = "Haryana"

DISTRICT = "Sirsa"

TEHSIL = "Kalanwali"

VILLAGES = [
    "Taruana",
]

# ==========================================================
# Jamabandi Years
# ==========================================================

JAMABANDI_YEARS = [
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
]

# ==========================================================
# Owners
# ==========================================================

OWNER_NAMES = [
    "Mohinder Singh",
    "Gurmail Singh",
    "Baldev Singh",
    "Jaswant Singh",
    "Kuldeep Singh",
    "Ranjit Singh",
    "Darshan Singh",
    "Jagir Singh",
    "Harbans Singh",
    "Surjit Singh",
    "Rajinder Singh",
    "Paramjit Singh",
    "Jasbir Singh",
    "Sukhdev Singh",
    "Karnail Singh",
    "Harbans Kaur",
    "Surjit Kaur",
    "Paramjit Kaur",
    "Raj Kaur",
    "Manjit Kaur",
]

# ==========================================================
# Khewats
# ==========================================================

KHEWAT_NUMBERS = list(range(1, 21))

# ==========================================================
# Parcel Numbers
# ==========================================================

PARCELS = []

for rectangle in range(1, 21):

    for killa in range(1, 6):

        PARCELS.append(
            (
                rectangle,
                str(killa),
            )
        )

# ==========================================================
# Default Area
# ==========================================================

DEFAULT_KANAL = 8

DEFAULT_MARLA = 0

DEFAULT_SARSAI = 0