from app import evaluate

def test_business_rules():
    assert evaluate({'ev':80,'pv':100,'ac':100,'bac':200})['eac']==250
