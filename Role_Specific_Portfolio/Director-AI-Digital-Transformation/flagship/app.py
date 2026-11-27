def evaluate(x):
    benefit=x['hours']*x['rate']*x['adoption']
    return {'annual_benefit':benefit,'net_benefit':benefit-x['cost'],'roi':(benefit-x['cost'])/x['cost']}

if __name__ == '__main__':
    import json
    print(json.dumps(evaluate({'hours':2000,'rate':60,'adoption':.8,'cost':40000}),indent=2))
