import math
def evaluate(x):
    ident=x.get('id'); amount=x.get('amount')
    if not isinstance(ident,str) or not ident.strip() or isinstance(amount,bool) or not isinstance(amount,(int,float)) or not math.isfinite(amount) or amount<0: return {'status':400,'state':'invalid'}
    return {'status':202,'state':'review' if amount>=10000 else 'approved','request_id':ident}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({"id":"REQ-01","amount":15000}),indent=2))
