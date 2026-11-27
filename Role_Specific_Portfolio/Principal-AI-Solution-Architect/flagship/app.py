def evaluate(x):
    words=set(x['query'].lower().split())
    docs=[('P01','leave requests require manager approval'),('P02','expenses require receipts')]
    ranked=sorted(docs,key=lambda d:len(words & set(d[1].split())),reverse=True)
    return {'source':ranked[0][0],'answer':ranked[0][1]} if words & set(ranked[0][1].split()) else {'source':None,'answer':'Escalate to human'}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({'query':'leave approval'}),indent=2))
