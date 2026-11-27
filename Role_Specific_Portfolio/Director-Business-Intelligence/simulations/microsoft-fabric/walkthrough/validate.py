import csv
from pathlib import Path
from decimal import Decimal
with Path(__file__).with_name("sample.csv").open() as f:
    rows=list(csv.DictReader(f))
b=sum(Decimal(r["budget"]) for r in rows)
a=sum(Decimal(r["actual"]) for r in rows)
assert (len(rows),b,a,b-a)==(2,300,310,-10)
print(f"Rows={len(rows)} Budget={b} Actual={a} Variance={b-a}")
