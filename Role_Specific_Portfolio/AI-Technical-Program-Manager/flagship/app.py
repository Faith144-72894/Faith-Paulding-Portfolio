def evaluate(x):
    p,t,c=(x[k] for k in ('passed','total','critical'))
    if any(type(v) is not int for v in (p,t,c)) or t<=0 or not 0<=p<=t or not 0<=c<=t-p: raise ValueError('Invalid counts')
    rate=p/t
    return {'release':'approved' if rate>=.9 and c==0 else 'blocked','pass_rate':rate,'failed':t-p}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({"passed":95,"total":100,"critical":0}),indent=2))
