from app import evaluate

def test_business_rules():
    assert evaluate({'passed':90,'total':100,'critical':1})['release']=='blocked'
    assert evaluate({'passed':90,'total':100,'critical':0})['release']=='approved'
