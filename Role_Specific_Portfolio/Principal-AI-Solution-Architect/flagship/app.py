import re
DOCS={'P01':'leave requests require manager approval','P02':'expenses require receipts','P03':'restricted records require security authorization'}
def evaluate(x):
    q=x['query']
    if not isinstance(q,str) or not q.strip(): raise ValueError('Query required')
    words=set(re.findall(r'\w+',q.lower()))-{'the','a','is','what','how','do','i','require'}
    scores=sorted(((len(words & set(re.findall(r'\w+',v))),k,v) for k,v in DOCS.items()),reverse=True)
    score,k,v=scores[0]
    if not score or (len(scores)>1 and scores[1][0]==score): return {'source':None,'answer':'Escalate to human'}
    return {'source':k,'answer':v,'matched_terms':score,'method':'lexical retrieval'}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({"query":"leave approval"}),indent=2))
