"""
Haryana Revenue Toolkit (HRTK)

Development Sample Data.
"""

from __future__ import annotations

# ---------------------------------------------------------
# Geography
# ---------------------------------------------------------

STATE = "Haryana"

DISTRICT = "Sirsa"

TEHSIL = "Kalanwali"

VILLAGE = {
    "code": "V001",
    "name": "Taruana",
}

# ---------------------------------------------------------
# Owners
# ---------------------------------------------------------

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

# ---------------------------------------------------------
# Khewats
# ---------------------------------------------------------

KHEWAT_NUMBERS = [
    str(i)
    for i in range(1, 21)
]

# ---------------------------------------------------------
# Jamabandi
# ---------------------------------------------------------

JAMABANDI_YEAR = "2024-25"

# ---------------------------------------------------------
# Parcels
# ---------------------------------------------------------

DEFAULT_KANAL = 8
DEFAULT_MARLA = 0
DEFAULT_SARSAI = 0