import pytest
from app import *

def test_case_1():
    assert evaluate({'passed':95,'total':100,'critical':0})['release']=='approved'

def test_case_2():
    assert evaluate({'passed':90,'total':100,'critical':1})['release']=='blocked'

def test_case_3():
    with pytest.raises(ValueError):
        evaluate({'passed':0,'total':0,'critical':0})

def test_case_4():
    with pytest.raises(ValueError):
        evaluate({'passed':101,'total':100,'critical':0})

