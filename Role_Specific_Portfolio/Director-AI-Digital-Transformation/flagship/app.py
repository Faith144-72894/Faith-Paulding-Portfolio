import math
def evaluate(x):
    h,r,a,c=(x[k] for k in ('hours','rate','adoption','cost'))
    if not all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) for v in (h,r,a,c)) or min(h,r)<0 or not 0<=a<=1 or c<=0: raise ValueError('Invalid investment assumptions')
    benefit=h*r*a
    return {'annual_benefit':benefit,'net_benefit':benefit-c,'roi':(benefit-c)/c,'scenarios':{str(v): (h*r*v-c)/c for v in (.25,.5,.75,1)},'break_even_adoption':c/(h*r) if h*r else None}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({"hours":2000,"rate":60,"adoption":0.8,"cost":40000}),indent=2))
