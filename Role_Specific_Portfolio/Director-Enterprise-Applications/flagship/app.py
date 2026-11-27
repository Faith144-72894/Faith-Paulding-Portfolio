def evaluate(x):
    if not x.get('id') or x.get('amount',-1)<0: return {'status':400,'state':'invalid'}
    return {'status':202,'state':'review' if x['amount']>=10000 else 'approved','request_id':x['id']}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({'id':'REQ-01','amount':15000}),indent=2))
