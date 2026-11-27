from app import evaluate

def test_business_rules():
    assert evaluate({'hours':100,'rate':10,'adoption':.5,'cost':1000})['roi']==-.5
