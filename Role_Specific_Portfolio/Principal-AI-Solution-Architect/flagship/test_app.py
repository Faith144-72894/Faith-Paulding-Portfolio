from app import evaluate

def test_business_rules():
    assert evaluate({'query':'leave'})['source']=='P01'
    assert evaluate({'query':'unknown'})['source'] is None
