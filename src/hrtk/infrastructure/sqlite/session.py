"""
Haryana Revenue Toolkit (HRTK)

SQLite Session Factory.
"""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ---------------------------------------------------------
# Database Location
# ---------------------------------------------------------

DATABASE_FILE = (
    Path.home()
    / ".hrtk"
    / "hrtk.db"
)

DATABASE_FILE.parent.mkdir(
    parents=True,
    exist_ok=True,
)

DATABASE_URL = (
    f"sqlite:///{DATABASE_FILE}"
)

# ---------------------------------------------------------
# Engine
# ---------------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    future=True,
)

# ---------------------------------------------------------
# Session Factory
# ---------------------------------------------------------

SessionFactory = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)