from app import evaluate

def test_business_rules():
    assert evaluate({'tasks':{'A':{'days':3,'deps':[]},'B':{'days':5,'deps':['A']}}})['duration']==8
