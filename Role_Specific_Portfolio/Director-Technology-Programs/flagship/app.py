def evaluate(x):
    ev,pv,ac,bac=(x[k] for k in ('ev','pv','ac','bac'));return {'cpi':ev/ac,'spi':ev/pv,'eac':bac/(ev/ac),'cv':ev-ac,'sv':ev-pv}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({'ev':80000,'pv':100000,'ac':90000,'bac':200000}),indent=2))
