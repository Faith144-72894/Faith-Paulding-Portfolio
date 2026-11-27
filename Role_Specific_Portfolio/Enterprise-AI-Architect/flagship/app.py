def evaluate(x):
    classification=x.get('classification'); approved=x.get('approved')
    if classification not in ('public','internal','restricted') or type(approved) is not bool: return {'route':'deny','reason':'invalid policy input'}
    if classification=='restricted':return {'route':'deny','reason':'restricted classification'}
    if not approved:return {'route':'human review','reason':'approval required'}
    return {'route':'approved endpoint','reason':'policy checks passed'}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({"classification":"internal","approved":True}),indent=2))
