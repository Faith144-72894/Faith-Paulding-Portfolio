import sqlite3
def evaluate(x):
    db=sqlite3.connect(':memory:');db.execute('create table fact(program text,budget real,actual real)');db.executemany('insert into fact values(?,?,?)',x['rows']);r=db.execute('select sum(budget),sum(actual),sum(budget-actual) from fact').fetchone();db.close();return dict(zip(['budget','actual','variance'],r))

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({'rows':[('A',100,90),('B',200,220)]}),indent=2))
