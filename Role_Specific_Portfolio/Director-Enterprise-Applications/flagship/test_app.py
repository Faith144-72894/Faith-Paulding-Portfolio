from app import evaluate

def test_business_rules():
    assert evaluate({'id':'X','amount':10000})['state']=='review'
    assert evaluate({'amount':1})['status']==400
