import math
def evaluate(x):
    tasks=x['tasks']; finish={}; paths={}; visiting=set()
    if not tasks: raise ValueError('Tasks required')
    def visit(k):
        if k not in tasks: raise ValueError('Unknown dependency')
        if k in visiting: raise ValueError('Cycle')
        if k in finish:return finish[k]
        visiting.add(k); t=tasks[k]; days=t['days']
        if not isinstance(days,(int,float)) or not math.isfinite(days) or days<0: raise ValueError('Invalid duration')
        deps=t['deps']; prior=max(deps,key=visit) if deps else None
        finish[k]=days+(finish[prior] if prior is not None else 0)
        paths[k]=(paths[prior] if prior is not None else [])+[k]; visiting.remove(k); return finish[k]
    for k in tasks:visit(k)
    end=max(finish,key=finish.get)
    return {'finish_days':finish,'duration':finish[end],'critical_path':paths[end]}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({"tasks":{"A":{"days":3,"deps":[]},"B":{"days":5,"deps":["A"]}}}),indent=2))
