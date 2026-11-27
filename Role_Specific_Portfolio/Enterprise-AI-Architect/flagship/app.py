def evaluate(x):
    if x['classification']=='restricted':return {'route':'deny'}
    if not x['approved']:return {'route':'human review'}
    return {'route':'approved endpoint'}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({'classification':'internal','approved':True}),indent=2))
