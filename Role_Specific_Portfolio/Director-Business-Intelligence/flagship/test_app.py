import pytest
from app import *

def test_case_1():
    assert evaluate({'rows':[('A',100,90),('B',200,220)]})['variance']==-10

def test_case_2():
    assert evaluate({'rows':[]})['budget']==0

def test_case_3():
    with pytest.raises(ValueError):
        evaluate({'rows':[('A',-1,0)]})

def test_case_4():
    assert load_csv('sample.csv')['variance']==-10

