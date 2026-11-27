from app import evaluate

def test_business_rules():
    assert evaluate({'classification':'restricted','approved':True})['route']=='deny'
    assert evaluate({'classification':'public','approved':False})['route']=='human review'
