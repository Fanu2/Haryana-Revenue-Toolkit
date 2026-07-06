from pathlib import Path
import sqlite3

db = Path.home() / ".hrtk" / "hrtk.db"

print("=" * 60)
print(f"Database : {db}")
print("=" * 60)

conn = sqlite3.connect(db)
cur = conn.cursor()

cur.execute(
    "SELECT name FROM sqlite_master "
    "WHERE type='table' "
    "ORDER BY name"
)

tables = [row[0] for row in cur.fetchall()]

print()

for table in tables:
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    count = cur.fetchone()[0]
    print(f"{table:<30} {count}")

conn.close()