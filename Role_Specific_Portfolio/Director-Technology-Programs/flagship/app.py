import math
def evaluate(x):
    ev,pv,ac,bac=(x[k] for k in ('ev','pv','ac','bac'))
    if not all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) and v>=0 for v in (ev,pv,ac,bac)) or bac<=0: raise ValueError('Invalid earned value inputs')
    cpi=ev/ac if ac else None; spi=ev/pv if pv else None
    return {'cpi':cpi,'spi':spi,'eac':bac/cpi if cpi else None,'cv':ev-ac,'sv':ev-pv,'eac_budget_rate':ac+bac-ev}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({"ev":80000,"pv":100000,"ac":90000,"bac":200000}),indent=2))
