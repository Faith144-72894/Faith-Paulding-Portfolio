def evaluate(x):
    return {'release': 'approved' if x['passed']/x['total'] >= .9 and x['critical']==0 else 'blocked', 'pass_rate':x['passed']/x['total']}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({'passed':95,'total':100,'critical':0}),indent=2))
