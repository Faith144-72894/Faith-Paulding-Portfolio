import sqlite3,csv,math
from contextlib import closing
def evaluate(x):
    rows=x['rows']
    if any(len(row)!=3 or not row[0] or any(not isinstance(v,(int,float)) or not math.isfinite(v) or v<0 for v in row[1:]) for row in rows): raise ValueError('Invalid fact row')
    with closing(sqlite3.connect(':memory:')) as db:
        db.execute('create table fact(program text,budget real,actual real)')
        db.executemany('insert into fact values(?,?,?)',rows)
        r=db.execute('select coalesce(sum(budget),0),coalesce(sum(actual),0),coalesce(sum(budget-actual),0) from fact').fetchone()
        return dict(zip(['budget','actual','variance'],r))
def load_csv(path):
    with open(path,newline='') as f:
        return evaluate({'rows':[(r['program'],float(r['budget']),float(r['actual'])) for r in csv.DictReader(f)]})

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({"rows":[["A",100,90],["B",200,220]]}),indent=2))
