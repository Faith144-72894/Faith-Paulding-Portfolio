def evaluate(x):
    tasks=x['tasks']; finish={}; visiting=set()
    def visit(k):
        if k in visiting: raise ValueError('Cycle')
        if k in finish:return finish[k]
        visiting.add(k); t=tasks[k]; finish[k]=t['days']+max([visit(d) for d in t['deps']] or [0]); visiting.remove(k); return finish[k]
    for k in tasks:visit(k)
    return {'finish_days':finish,'duration':max(finish.values())}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({'tasks':{'A':{'days':3,'deps':[]},'B':{'days':5,'deps':['A']}}}),indent=2))
