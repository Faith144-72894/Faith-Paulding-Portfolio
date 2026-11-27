from app import evaluate

def test_business_rules():
    assert evaluate({'rows':[('A',100,90),('B',200,220)]})['variance']==-10
